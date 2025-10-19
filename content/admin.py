from django.contrib import admin
from .models import Subject, Topic, Video, Document, Tip, QuizQuestion, QuizOption


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ["name"]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_filter = ["subject"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "topic", "created_at")
    list_filter = ("subject", "topic")
    search_fields = ("title",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "topic", "created_at")
    list_filter = ("subject", "topic")
    search_fields = ("title",)


class QuizOptionInline(admin.TabularInline):
    model = QuizOption
    extra = 2


@admin.register(QuizQuestion)
class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "subject", "topic", "created_at")
    list_filter = ("subject", "topic")
    search_fields = ("text",)
    inlines = [QuizOptionInline]


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ("content", "subject", "topic", "created_at")
    list_filter = ("subject", "topic")
    search_fields = ("content",)
