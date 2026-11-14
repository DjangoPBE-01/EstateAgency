from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import Category, Course, Module, Video, Comment, CourseCertificate


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1
    fields = ('order', 'name', 'description')
    ordering = ('order',)


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('order', 'title', 'video_file', 'period_time', 'status')
    ordering = ('order',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'author', 'category', 'price', 'is_active', 'created_at')
    list_filter = ('is_active', 'category', 'created_at')
    search_fields = ('title', 'author', 'description')
    list_editable = ('price', 'is_active')
    autocomplete_fields = ['category', 'promo_code']
    inlines = [ModuleInline]

    def get_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="35" style="border-radius: 4px; object-fit: cover;" />', obj.image.url)
        return "-"
    get_image.short_description = _('Image')


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'order', 'created_at')
    list_filter = ('course',)
    search_fields = ('name', 'course__title')
    list_editable = ('order',)
    autocomplete_fields = ['course']
    inlines = [VideoInline]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'order', 'period_time', 'status', 'created_at')
    list_filter = ('status', 'module__course', 'created_at')
    search_fields = ('title', 'module__name', 'description')
    list_editable = ('order', 'status')
    autocomplete_fields = ['module']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'review', 'short_content', 'created_at')
    list_filter = ('review', 'course', 'created_at')
    search_fields = ('user__username', 'course__title', 'content')
    autocomplete_fields = ['user', 'course']

    def short_content(self, obj):
        if obj.content:
            return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
        return "-"
    short_content.short_description = _('Content')


@admin.register(CourseCertificate)
class CourseCertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'course', 'created_at')
    list_filter = ('course', 'created_at')
    search_fields = ('name', 'user__username', 'course__title')
    autocomplete_fields = ['user', 'course']
