from django.contrib import admin
from django.utils.html import format_html
from .models import Band

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'url', 'has_logo', 'has_cover')
    search_fields = ('name', 'email')
    readonly_fields = ('logo_preview', 'cover_photo_preview')
    fieldsets = (
        (None, {
            'fields': ('name', 'url', 'bio')
        }),
        ('Email Configuration', {
            'fields': ('email', 'email_password', 'smtp_server', 'smtp_port'),
            'description': 'Configure email settings for the contact form',
            'classes': ('collapse',)  # Makes this section collapsible for security
        }),
        ('Logo', {
            'fields': ('logo', 'logo_alt', 'logo_preview'),
            'description': 'Upload and manage the band\'s logo'
        }),
        ('Cover Photo', {
            'fields': ('cover_photo', 'cover_photo_alt', 'cover_photo_preview'),
            'description': 'Upload and manage the band\'s cover photo'
        })
    )
    
    def has_logo(self, obj):
        return bool(obj.logo)
    has_logo.boolean = True
    
    def has_cover(self, obj):
        return bool(obj.cover_photo)
    has_cover.boolean = True

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.logo.url)
        return "No logo uploaded"
    logo_preview.short_description = 'Logo Preview'

    def cover_photo_preview(self, obj):
        if obj.cover_photo:
            return format_html('<img src="{}" style="max-height: 200px;" />', obj.cover_photo.url)
        return "No cover photo uploaded"
    cover_photo_preview.short_description = 'Cover Photo Preview'

    def save_model(self, request, obj, form, change):
        # Handle image deletion
        if 'logo' in form.cleaned_data and not form.cleaned_data['logo']:
            # Logo was cleared
            if obj.logo:
                obj.logo.delete(save=False)
        if 'cover_photo' in form.cleaned_data and not form.cleaned_data['cover_photo']:
            # Cover photo was cleared
            if obj.cover_photo:
                obj.cover_photo.delete(save=False)
        super().save_model(request, obj, form, change)
