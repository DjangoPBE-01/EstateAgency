from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Interest, UserInterest, PromoCode


class UserInterestInline(admin.TabularInline):
    model = UserInterest
    extra = 1
    autocomplete_fields = ['interest']


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'get_photo', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'deleted_reason')
    search_fields = ('username', 'email', 'phone_number', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    inlines = [UserInterestInline]

    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Info'), {
            'fields': ('phone_number', 'bio', 'photo', 'deleted_reason')
        }),
    )

    def get_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="35" height="35" style="border-radius: 50%; object-fit: cover;" />', obj.photo.url)
        return "-"
    get_photo.short_description = _('Photo')


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


@admin.register(UserInterest)
class UserInterestAdmin(admin.ModelAdmin):
    list_display = ('user', 'interest', 'created_at')
    list_filter = ('interest', 'created_at')
    search_fields = ('user__username', 'interest__name')
    autocomplete_fields = ['user', 'interest']


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percentage', 'valid_from', 'valid_to', 'is_active', 'is_used', 'user')
    list_filter = ('is_active', 'is_used', 'valid_from', 'valid_to')
    search_fields = ('code', 'user__username', 'description')
    list_editable = ('is_active',)
    autocomplete_fields = ['user']
