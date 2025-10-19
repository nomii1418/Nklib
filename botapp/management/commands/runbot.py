import asyncio
import os
import django
from django.conf import settings
from django.db import transaction
from django.core.files.base import ContentFile

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mechlib.settings")
django.setup()

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, InputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
import requests

from content.models import Subject, Topic, Document, Video, Tip, QuizQuestion, QuizOption
from botapp.models import BotAdmin


class AddSubject(StatesGroup):
    waiting_name = State()


class AddTopic(StatesGroup):
    choosing_subject = State()
    waiting_name = State()


class AddTip(StatesGroup):
    choosing_subject = State()
    choosing_topic = State()
    waiting_content = State()


class UploadDoc(StatesGroup):
    choosing_subject = State()
    choosing_topic = State()
    waiting_file = State()


class AddVideoUrl(StatesGroup):
    choosing_subject = State()
    choosing_topic = State()
    waiting_title = State()
    waiting_url = State()


class AddQuiz(StatesGroup):
    choosing_subject = State()
    choosing_topic = State()
    waiting_question = State()
    waiting_option1 = State()
    waiting_option2 = State()
    waiting_option3 = State()
    waiting_option4 = State()
    waiting_correct = State()


async def is_admin(user_id: int) -> bool:
    return await asyncio.to_thread(lambda: BotAdmin.objects.filter(telegram_user_id=user_id).exists())


def admin_menu_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Add Subject", callback_data="add_subject")],
        [InlineKeyboardButton(text="Add Topic", callback_data="add_topic")],
        [InlineKeyboardButton(text="Upload Document", callback_data="upload_doc")],
        [InlineKeyboardButton(text="Add Tip", callback_data="add_tip")],
        [InlineKeyboardButton(text="Add Video URL", callback_data="add_video")],
        [InlineKeyboardButton(text="Add Quiz", callback_data="add_quiz")],
        [InlineKeyboardButton(text="Manage Subjects", callback_data="manage_subs")],
        [InlineKeyboardButton(text="Manage Content", callback_data="manage_content")],
    ])


def subjects_kb():
    buttons = [[InlineKeyboardButton(text=s.name, callback_data=f"sub:{s.id}")] for s in Subject.objects.order_by('name')]
    buttons.append([InlineKeyboardButton(text="Cancel", callback_data="cancel")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def topics_kb(subject_id: int):
    topics = Topic.objects.filter(subject_id=subject_id).order_by('name')
    buttons = [[InlineKeyboardButton(text=t.name, callback_data=f"top:{t.id}")] for t in topics]
    buttons.append([InlineKeyboardButton(text="No Topic", callback_data="top:0")])
    buttons.append([InlineKeyboardButton(text="Cancel", callback_data="cancel")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


async def start_handler(message: Message):
    await message.answer("Welcome to Mechanical Library! Use /admin for admin menu or browse the website.")


async def admin_handler(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) == 2:
        password = args[1].strip()
        if password == (settings.BOT_ADMIN_PASS or "nom"):
            await asyncio.to_thread(BotAdmin.objects.get_or_create, telegram_user_id=message.from_user.id)
            await message.answer("Admin access granted.", reply_markup=admin_menu_kb())
        else:
            await message.answer("Invalid admin password.")
    else:
        if await is_admin(message.from_user.id):
            await message.answer("Admin panel:", reply_markup=admin_menu_kb())
        else:
            await message.answer("Send /admin <password> to gain admin access.")


async def callback_router(callback: CallbackQuery, state: FSMContext):
    if not await is_admin(callback.from_user.id):
        await callback.answer("Admin only", show_alert=True)
        return
    data = callback.data
    if data == "add_subject":
        await state.set_state(AddSubject.waiting_name)
        await callback.message.answer("Send subject name:")
        await callback.answer()
    elif data == "add_topic":
        await state.set_state(AddTopic.choosing_subject)
        await callback.message.answer("Choose subject:", reply_markup=subjects_kb())
        await callback.answer()
    elif data == "upload_doc":
        await state.set_state(UploadDoc.choosing_subject)
        await callback.message.answer("Choose subject:", reply_markup=subjects_kb())
        await callback.answer()
    elif data == "add_tip":
        await state.set_state(AddTip.choosing_subject)
        await callback.message.answer("Choose subject:", reply_markup=subjects_kb())
        await callback.answer()
    elif data == "add_video":
        await state.set_state(AddVideoUrl.choosing_subject)
        await callback.message.answer("Choose subject:", reply_markup=subjects_kb())
        await callback.answer()
    elif data == "add_quiz":
        await state.set_state(AddQuiz.choosing_subject)
        await callback.message.answer("Choose subject:", reply_markup=subjects_kb())
        await callback.answer()
    elif data == "cancel":
        await state.clear()
        await callback.message.answer("Cancelled.")
        await callback.answer()
    elif data == "manage_subs":
        await callback.message.answer("Select subject to manage:", reply_markup=subjects_kb())
        await callback.answer()
    elif data == "manage_content":
        await callback.message.answer("Select subject to manage content:", reply_markup=subjects_kb())
        await callback.answer()
    elif data.startswith("sub:"):
        sub_id = int(data.split(":")[1])
        current = await state.get_state()
        await state.update_data(subject_id=sub_id)
        if current == AddTopic.choosing_subject.state:
            await state.set_state(AddTopic.waiting_name)
            await callback.message.answer("Send topic name:")
        elif current == UploadDoc.choosing_subject.state:
            await state.set_state(UploadDoc.choosing_topic)
            await callback.message.answer("Choose topic:", reply_markup=topics_kb(sub_id))
        elif current == AddTip.choosing_subject.state:
            await state.set_state(AddTip.choosing_topic)
            await callback.message.answer("Choose topic:", reply_markup=topics_kb(sub_id))
        elif current == AddVideoUrl.choosing_subject.state:
            await state.set_state(AddVideoUrl.choosing_topic)
            await callback.message.answer("Choose topic:", reply_markup=topics_kb(sub_id))
        elif current == AddQuiz.choosing_subject.state:
            await state.set_state(AddQuiz.choosing_topic)
            await callback.message.answer("Choose topic:", reply_markup=topics_kb(sub_id))
        else:
            # Management menus
            kb = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="List Documents", callback_data=f"list_docs:{sub_id}")],
                [InlineKeyboardButton(text="List Videos", callback_data=f"list_vids:{sub_id}")],
                [InlineKeyboardButton(text="List Tips", callback_data=f"list_tips:{sub_id}")],
                [InlineKeyboardButton(text="List Quiz", callback_data=f"list_quiz:{sub_id}")],
                [InlineKeyboardButton(text="Delete Subject", callback_data=f"delsub:{sub_id}")],
                [InlineKeyboardButton(text="Cancel", callback_data="cancel")],
            ])
            await callback.message.answer("Subject actions:", reply_markup=kb)
        await callback.answer()
    elif data.startswith("top:"):
        top_id = int(data.split(":")[1])
        if top_id == 0:
            top_id = None
        await state.update_data(topic_id=top_id)
        current = await state.get_state()
        if current == UploadDoc.choosing_topic.state:
            await state.set_state(UploadDoc.waiting_file)
            await callback.message.answer("Send the file (as Document):")
        elif current == AddTip.choosing_topic.state:
            await state.set_state(AddTip.waiting_content)
            await callback.message.answer("Send the tip content:")
        elif current == AddVideoUrl.choosing_topic.state:
            await state.set_state(AddVideoUrl.waiting_title)
            await callback.message.answer("Send the video title:")
        elif current == AddQuiz.choosing_topic.state:
            await state.set_state(AddQuiz.waiting_question)
            await callback.message.answer("Send the quiz question:")
        await callback.answer()
    elif data.startswith("delsub:"):
        sub_id = int(data.split(":")[1])
        def work():
            try:
                Subject.objects.get(id=sub_id).delete()
                return True
            except Subject.DoesNotExist:
                return False
        ok = await asyncio.to_thread(work)
        await callback.message.answer("Subject deleted." if ok else "Subject not found.")
        await callback.answer()
    elif data.startswith("list_docs:"):
        sub_id = int(data.split(":")[1])
        docs = list(Document.objects.filter(subject_id=sub_id).order_by('-created_at')[:20])
        if not docs:
            await callback.message.answer("No documents.")
            await callback.answer()
        else:
            rows = []
            for d in docs:
                rows.append([InlineKeyboardButton(text=(d.title[:48] or str(d.id)), callback_data=f"noop")])
                rows.append([
                    InlineKeyboardButton(text="Link", callback_data=f"doclink:{d.id}"),
                    InlineKeyboardButton(text="Edit", callback_data=f"editdoc:{d.id}"),
                    InlineKeyboardButton(text="Delete", callback_data=f"docdel:{d.id}"),
                ])
            rows.append([InlineKeyboardButton(text="Close", callback_data="cancel")])
            await callback.message.answer("Documents:", reply_markup=InlineKeyboardMarkup(inline_keyboard=rows))
            await callback.answer()
    elif data.startswith("doclink:"):
        doc_id = int(data.split(":")[1])
        try:
            doc = Document.objects.get(id=doc_id)
            base = settings.PUBLIC_BASE_URL.rstrip('/') if settings.PUBLIC_BASE_URL else ''
            link = f"{base}{doc.file.url}"
            await callback.message.answer(f"Link: {link}")
        except Document.DoesNotExist:
            await callback.message.answer("Document not found.")
        await callback.answer()
    elif data.startswith("docdel:"):
        doc_id = int(data.split(":")[1])
        def work():
            try:
                Document.objects.get(id=doc_id).delete()
                return True
            except Document.DoesNotExist:
                return False
        ok = await asyncio.to_thread(work)
        await callback.message.answer("Document deleted." if ok else "Document not found.")
        await callback.answer()
    elif data.startswith("editdoc:"):
        doc_id = int(data.split(":")[1])
        await state.update_data(edit_doc_id=doc_id)
        await callback.message.answer("Send new document title:")
        await state.set_state(EditDocTitle.waiting_title)
        await callback.answer()
    elif data.startswith("list_vids:"):
        sub_id = int(data.split(":")[1])
        vids = list(Video.objects.filter(subject_id=sub_id).order_by('-created_at')[:20])
        if not vids:
            await callback.message.answer("No videos.")
            await callback.answer()
        else:
            rows = []
            for v in vids:
                rows.append([InlineKeyboardButton(text=(v.title[:48] or str(v.id)), callback_data=f"noop")])
                rows.append([
                    InlineKeyboardButton(text="Open", callback_data=f"vidlink:{v.id}"),
                    InlineKeyboardButton(text="Edit", callback_data=f"editvid:{v.id}"),
                    InlineKeyboardButton(text="Delete", callback_data=f"viddel:{v.id}"),
                ])
            rows.append([InlineKeyboardButton(text="Close", callback_data="cancel")])
            await callback.message.answer("Videos:", reply_markup=InlineKeyboardMarkup(inline_keyboard=rows))
            await callback.answer()
    elif data.startswith("vidlink:"):
        vid_id = int(data.split(":")[1])
        try:
            v = Video.objects.get(id=vid_id)
            if v.url:
                await callback.message.answer(f"URL: {v.url}")
            elif v.file:
                base = settings.PUBLIC_BASE_URL.rstrip('/') if settings.PUBLIC_BASE_URL else ''
                link = f"{base}{v.file.url}"
                await callback.message.answer(f"Link: {link}")
            else:
                await callback.message.answer("No link available.")
        except Video.DoesNotExist:
            await callback.message.answer("Video not found.")
        await callback.answer()
    elif data.startswith("viddel:"):
        vid_id = int(data.split(":")[1])
        def work():
            try:
                Video.objects.get(id=vid_id).delete()
                return True
            except Video.DoesNotExist:
                return False
        ok = await asyncio.to_thread(work)
        await callback.message.answer("Video deleted." if ok else "Video not found.")
        await callback.answer()
    elif data.startswith("editvid:"):
        vid_id = int(data.split(":")[1])
        await state.update_data(edit_video_id=vid_id)
        await callback.message.answer("Send new video title:")
        await state.set_state(EditVideoTitle.waiting_title)
        await callback.answer()
    elif data.startswith("list_tips:"):
        sub_id = int(data.split(":")[1])
        tips = list(Tip.objects.filter(subject_id=sub_id).order_by('-created_at')[:20])
        if not tips:
            await callback.message.answer("No tips.")
            await callback.answer()
        else:
            rows = []
            for t in tips:
                rows.append([InlineKeyboardButton(text=(t.content[:48] or str(t.id)), callback_data=f"noop")])
                rows.append([
                    InlineKeyboardButton(text="Edit", callback_data=f"edittip:{t.id}"),
                    InlineKeyboardButton(text="Delete", callback_data=f"tipdel:{t.id}"),
                ])
            rows.append([InlineKeyboardButton(text="Close", callback_data="cancel")])
            await callback.message.answer("Tips:", reply_markup=InlineKeyboardMarkup(inline_keyboard=rows))
            await callback.answer()
    elif data.startswith("tipdel:"):
        tip_id = int(data.split(":")[1])
        def work():
            try:
                Tip.objects.get(id=tip_id).delete()
                return True
            except Tip.DoesNotExist:
                return False
        ok = await asyncio.to_thread(work)
        await callback.message.answer("Tip deleted." if ok else "Tip not found.")
        await callback.answer()
    elif data.startswith("edittip:"):
        tip_id = int(data.split(":")[1])
        await state.update_data(edit_tip_id=tip_id)
        await callback.message.answer("Send new tip content:")
        await state.set_state(EditTip.waiting_content)
        await callback.answer()
    elif data.startswith("list_quiz:"):
        sub_id = int(data.split(":")[1])
        qs = list(QuizQuestion.objects.filter(subject_id=sub_id).order_by('-created_at')[:20])
        if not qs:
            await callback.message.answer("No quiz questions.")
            await callback.answer()
        else:
            rows = []
            for q in qs:
                rows.append([InlineKeyboardButton(text=(q.text[:48] or str(q.id)), callback_data=f"noop")])
                rows.append([
                    InlineKeyboardButton(text="Delete", callback_data=f"quizdel:{q.id}"),
                ])
            rows.append([InlineKeyboardButton(text="Close", callback_data="cancel")])
            await callback.message.answer("Quiz questions:", reply_markup=InlineKeyboardMarkup(inline_keyboard=rows))
            await callback.answer()
    elif data.startswith("quizdel:"):
        qid = int(data.split(":")[1])
        def work():
            try:
                QuizQuestion.objects.get(id=qid).delete()
                return True
            except QuizQuestion.DoesNotExist:
                return False
        ok = await asyncio.to_thread(work)
        await callback.message.answer("Quiz question deleted." if ok else "Quiz question not found.")
        await callback.answer()


async def add_subject_name(message: Message, state: FSMContext):
    name = message.text.strip()
    def work():
        return Subject.objects.get_or_create(name=name)
    subj, _ = await asyncio.to_thread(work)
    await message.answer(f"Created subject: {subj.name}")
    await state.clear()


async def add_topic_name(message: Message, state: FSMContext):
    data = await state.get_data()
    subject_id = data.get("subject_id")
    name = message.text.strip()
    def work():
        subject = Subject.objects.get(id=subject_id)
        topic, _ = Topic.objects.get_or_create(subject=subject, name=name)
        return topic
    topic = await asyncio.to_thread(work)
    await message.answer(f"Created topic: {topic.name}")
    await state.clear()


async def add_tip_content(message: Message, state: FSMContext):
    data = await state.get_data()
    subject_id = data.get("subject_id")
    topic_id = data.get("topic_id")
    content = message.text.strip()
    def work():
        subject = Subject.objects.get(id=subject_id)
        topic = Topic.objects.get(id=topic_id) if topic_id else None
        return Tip.objects.create(subject=subject, topic=topic, content=content)
    tip = await asyncio.to_thread(work)
    await message.answer(f"Saved tip under subject: {tip.subject.name}")
    await state.clear()


async def add_video_title(message: Message, state: FSMContext):
    await state.update_data(video_title=message.text.strip())
    await state.set_state(AddVideoUrl.waiting_url)
    await message.answer("Send the video URL (YouTube etc):")


async def add_video_url(message: Message, state: FSMContext):
    data = await state.get_data()
    subject_id = data.get("subject_id")
    topic_id = data.get("topic_id")
    title = data.get("video_title")
    url = message.text.strip()
    def work():
        subject = Subject.objects.get(id=subject_id)
        topic = Topic.objects.get(id=topic_id) if topic_id else None
        return Video.objects.create(subject=subject, topic=topic, title=title, url=url)
    video = await asyncio.to_thread(work)
    await message.answer(f"Saved video: {video.title}")
    await state.clear()


async def upload_doc_file(message: Message, state: FSMContext, bot: Bot):
    if not message.document:
        await message.answer("Please send a file as Document.")
        return
    data = await state.get_data()
    subject_id = data.get("subject_id")
    topic_id = data.get("topic_id")

    file_id = message.document.file_id
    file_name = message.document.file_name or "upload.bin"
    file = await bot.get_file(file_id)

    file_size = message.document.file_size or 0
    # Build file URL
    file_path = file.file_path
    url = f"https://api.telegram.org/file/bot{settings.TELEGRAM_BOT_TOKEN}/{file_path}"

    sent = await message.answer("Downloading: 0%")

    # Stream download and update progress
    bytes_read = 0
    content = bytearray()
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        chunk_size = 1024 * 128
        for chunk in r.iter_content(chunk_size=chunk_size):
            if not chunk:
                continue
            content.extend(chunk)
            bytes_read += len(chunk)
            if file_size:
                pct = int(bytes_read * 100 / file_size)
                try:
                    await sent.edit_text(f"Downloading: {pct}%")
                except Exception:
                    pass

    await sent.edit_text("Saving file...")
    def work():
        subject = Subject.objects.get(id=subject_id)
        topic = Topic.objects.get(id=topic_id) if topic_id else None
        django_file = ContentFile(bytes(content), name=file_name)
        doc = Document.objects.create(subject=subject, topic=topic, title=file_name, file=django_file)
        return doc
    doc = await asyncio.to_thread(work)

    base = settings.PUBLIC_BASE_URL.rstrip('/') if settings.PUBLIC_BASE_URL else ''
    link = f"{base}{doc.file.url}"
    await sent.edit_text(f"Uploaded and saved. Link: {link}")
    await state.clear()


# Edit flows
class EditDocTitle(StatesGroup):
    waiting_title = State()


class EditVideoTitle(StatesGroup):
    waiting_title = State()


class EditTip(StatesGroup):
    waiting_content = State()


class AddQuizStateData:
    def __init__(self):
        self.subject_id = None
        self.topic_id = None
        self.question = None
        self.options = []


async def add_quiz_question(message: Message, state: FSMContext):
    await state.update_data(question=message.text.strip())
    await state.set_state(AddQuiz.waiting_option1)
    await message.answer("Option 1:")


async def add_quiz_option1(message: Message, state: FSMContext):
    await state.update_data(option1=message.text.strip())
    await state.set_state(AddQuiz.waiting_option2)
    await message.answer("Option 2:")


async def add_quiz_option2(message: Message, state: FSMContext):
    await state.update_data(option2=message.text.strip())
    await state.set_state(AddQuiz.waiting_option3)
    await message.answer("Option 3:")


async def add_quiz_option3(message: Message, state: FSMContext):
    await state.update_data(option3=message.text.strip())
    await state.set_state(AddQuiz.waiting_option4)
    await message.answer("Option 4:")


async def add_quiz_option4(message: Message, state: FSMContext):
    await state.update_data(option4=message.text.strip())
    await state.set_state(AddQuiz.waiting_correct)
    await message.answer("Which option is correct? (1-4)")


async def add_quiz_correct(message: Message, state: FSMContext):
    data = await state.get_data()
    subject_id = data.get("subject_id")
    topic_id = data.get("topic_id")
    question_text = data.get("question")
    options = [data.get("option1"), data.get("option2"), data.get("option3"), data.get("option4")]
    try:
        correct_index = int(message.text.strip()) - 1
        assert 0 <= correct_index <= 3
    except Exception:
        await message.answer("Please send a number between 1 and 4.")
        return

    def work():
        subject = Subject.objects.get(id=subject_id)
        topic = Topic.objects.get(id=topic_id) if topic_id else None
        q = QuizQuestion.objects.create(subject=subject, topic=topic, text=question_text)
        for idx, opt in enumerate(options):
            QuizOption.objects.create(question=q, text=opt, is_correct=(idx == correct_index))
        return q
    q = await asyncio.to_thread(work)
    await message.answer("Quiz saved.")
    await state.clear()


async def edit_doc_title_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    doc_id = data.get("edit_doc_id")
    new_title = message.text.strip()
    def work():
        try:
            d = Document.objects.get(id=doc_id)
            d.title = new_title
            d.save()
            return True
        except Document.DoesNotExist:
            return False
    ok = await asyncio.to_thread(work)
    await message.answer("Document title updated." if ok else "Document not found.")
    await state.clear()


async def edit_video_title_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    vid_id = data.get("edit_video_id")
    new_title = message.text.strip()
    def work():
        try:
            v = Video.objects.get(id=vid_id)
            v.title = new_title
            v.save()
            return True
        except Video.DoesNotExist:
            return False
    ok = await asyncio.to_thread(work)
    await message.answer("Video title updated." if ok else "Video not found.")
    await state.clear()


async def edit_tip_content_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    tip_id = data.get("edit_tip_id")
    new_content = message.text.strip()
    def work():
        try:
            t = Tip.objects.get(id=tip_id)
            t.content = new_content
            t.save()
            return True
        except Tip.DoesNotExist:
            return False
    ok = await asyncio.to_thread(work)
    await message.answer("Tip updated." if ok else "Tip not found.")
    await state.clear()


async def main():
    token = settings.TELEGRAM_BOT_TOKEN
    if not token:
        print("TELEGRAM_BOT_TOKEN not set. Exiting.")
        return
    bot = Bot(token=token)
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.register(start_handler, Command("start"))
    dp.message.register(admin_handler, Command("admin"))
    dp.callback_query.register(callback_router)

    dp.message.register(add_subject_name, AddSubject.waiting_name)
    dp.message.register(add_topic_name, AddTopic.waiting_name)
    dp.message.register(add_tip_content, AddTip.waiting_content)
    dp.message.register(add_video_title, AddVideoUrl.waiting_title)
    dp.message.register(add_video_url, AddVideoUrl.waiting_url)
    dp.message.register(upload_doc_file, UploadDoc.waiting_file)

    dp.message.register(add_quiz_question, AddQuiz.waiting_question)
    dp.message.register(add_quiz_option1, AddQuiz.waiting_option1)
    dp.message.register(add_quiz_option2, AddQuiz.waiting_option2)
    dp.message.register(add_quiz_option3, AddQuiz.waiting_option3)
    dp.message.register(add_quiz_option4, AddQuiz.waiting_option4)
    dp.message.register(add_quiz_correct, AddQuiz.waiting_correct)
    dp.message.register(edit_doc_title_handler, EditDocTitle.waiting_title)
    dp.message.register(edit_video_title_handler, EditVideoTitle.waiting_title)
    dp.message.register(edit_tip_content_handler, EditTip.waiting_content)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
