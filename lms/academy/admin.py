from django.contrib import admin
from .models import Product, Lesson, UserLesson


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'duration_seconds')


@admin.register(UserLesson)
class UserLessonAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'viewed', 'view_time_seconds')
