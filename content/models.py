from django.db import models
from django.utils.text import slugify


class Subject(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name)
            slug = base
            i = 1
            while Subject.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='topics')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("subject", "name")

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name)
            slug = base
            i = 1
            while Topic.objects.filter(subject=self.subject, slug=slug).exclude(pk=self.pk).exists():
                i += 1
                slug = f"{base}-{i}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.subject.name} / {self.name}"


class Video(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='videos')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True, related_name='videos')
    title = models.CharField(max_length=255)
    url = models.URLField(blank=True)
    file = models.FileField(upload_to='videos/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not self.url and not self.file:
            raise models.ValidationError("Provide either a URL or a file for the video.")

    def __str__(self) -> str:
        return self.title


class Document(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='documents')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True, related_name='documents')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='docs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Tip(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='tips')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True, related_name='tips')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Tip: {self.content[:40]}..."


class QuizQuestion(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='questions')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True, related_name='questions')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text[:60]


class QuizOption(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return ("* " if self.is_correct else "") + self.text
