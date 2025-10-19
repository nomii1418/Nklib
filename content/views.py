from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.http import require_POST
from django.conf import settings
from .models import Subject, Topic, Video, Document, Tip, QuizQuestion, QuizOption
import requests


def home(request):
    subjects = Subject.objects.order_by('name')
    return render(request, 'home.html', {"subjects": subjects})


def subject_detail(request, slug):
    subject = get_object_or_404(Subject, slug=slug)
    topics = subject.topics.order_by('name')
    videos = subject.videos.order_by('-created_at')[:20]
    documents = subject.documents.order_by('-created_at')[:20]
    tips = subject.tips.order_by('-created_at')[:20]
    questions = subject.questions.order_by('-created_at')[:20]
    return render(request, 'subject_detail.html', {
        "subject": subject,
        "topics": topics,
        "videos": videos,
        "documents": documents,
        "tips": tips,
        "questions": questions,
    })


def assistant_page(request):
    return render(request, 'assistant.html')


@require_POST
def assistant_ask(request):
    prompt = request.POST.get('prompt', '').strip()
    if not prompt:
        return JsonResponse({"ok": False, "error": "Empty prompt"}, status=400)

    # Try HF Inference API if configured
    api_key = settings.HUGGINGFACE_API_KEY
    model = settings.HUGGINGFACE_MODEL
    answer = None
    if api_key:
        try:
            headers = {"Authorization": f"Bearer {api_key}"}
            payload = {"inputs": prompt, "parameters": {"max_new_tokens": 256}}
            resp = requests.post(
                f"https://api-inference.huggingface.co/models/{model}",
                headers=headers,
                json=payload,
                timeout=30,
            )
            if resp.ok:
                data = resp.json()
                if isinstance(data, list) and data:
                    answer = data[0].get('generated_text')
                elif isinstance(data, dict) and 'generated_text' in data:
                    answer = data['generated_text']
        except Exception:
            answer = None

    # Fallback: naive search across tips and documents titles
    if not answer:
        tips = Tip.objects.filter(content__icontains=prompt)[:5]
        docs = Document.objects.filter(title__icontains=prompt)[:5]
        videos = Video.objects.filter(title__icontains=prompt)[:5]
        lines = []
        if tips:
            lines.append("Relevant tips:")
            for t in tips:
                lines.append(f"- {t.content[:140]}")
        if docs:
            lines.append("Relevant documents:")
            for d in docs:
                lines.append(f"- {d.title}")
        if videos:
            lines.append("Relevant videos:")
            for v in videos:
                lines.append(f"- {v.title} {v.url or ''}")
        if not lines:
            lines = ["I couldn't find AI results now. Try refining your query."]
        answer = "\n".join(lines)

    return JsonResponse({"ok": True, "answer": answer})


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_upload_page(request):
    subjects = Subject.objects.all().order_by('name')
    return render(request, 'admin_upload.html', {"subjects": subjects})


@login_required
@user_passes_test(lambda u: u.is_staff)
@require_POST
def admin_upload_submit(request):
    subject_id = request.POST.get('subject')
    topic_id = request.POST.get('topic')
    kind = request.POST.get('kind')  # 'document' or 'video'
    uploaded = request.FILES.get('file')
    title = request.POST.get('title') or (uploaded.name if uploaded else '')

    if not subject_id or not uploaded or kind not in ("document", "video"):
        return JsonResponse({"ok": False, "error": "Missing fields"}, status=400)

    subject = get_object_or_404(Subject, id=subject_id)
    topic = None
    if topic_id:
        try:
            topic = Topic.objects.get(id=topic_id, subject=subject)
        except Topic.DoesNotExist:
            topic = None

    if kind == 'document':
        obj = Document.objects.create(subject=subject, topic=topic, title=title, file=uploaded)
        link = obj.file.url
    else:
        obj = Video.objects.create(subject=subject, topic=topic, title=title, file=uploaded)
        link = obj.file.url

    return JsonResponse({"ok": True, "id": obj.id, "link": link})
