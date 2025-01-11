from django.contrib import admin
from .models import Music

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'band')
    list_filter = ('band',)
    search_fields = ('name',)
    fields = ('name', 'band', ('album_id', 'track_id'), 'bandcamp_url')
