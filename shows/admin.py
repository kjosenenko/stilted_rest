from typing import Literal

from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import SafeText
from django.utils.safestring import SafeText
from .models import Show, Venue

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'website_link')
    list_filter = ('state', 'city')
    search_fields = ('name', 'city')
    ordering = ('name',)

    def website_link(self, obj: Venue) -> SafeText | str:
        if obj.website:
            return format_html('<a href="{}" target="_blank">Visit Website</a>', obj.website)
        return "-"
    website_link.short_description = 'Website'  # type: ignore[attr-defined]

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('starts_at', 'venue', 'doors_display', 'ticket_price', 'has_presale', 'flyer_preview')
    list_filter = ('venue', 'starts_at')
    search_fields = ('venue__name', 'description', 'supporting_acts')
    autocomplete_fields: list[str] = ['venue']
    
    fieldsets: tuple[tuple[None, dict], tuple[Literal['Show Media'], dict], tuple[Literal['Ticket Information'], dict], tuple[Literal['Additional Information'], dict]] = (
        (None, {
            'fields': ('band', 'venue', ('doors_at', 'starts_at'))
        }),
        ('Show Media', {
            'fields': ('flyer',),
            'description': 'Upload a flyer image for the show. Clear the field to remove the current flyer.'
        }),
        ('Ticket Information', {
            'fields': ('ticket_price', 'presale_link', 'has_presale', 'age_restriction')
        }),
        ('Additional Information', {
            'fields': ('supporting_acts', 'description')
        }),
    )

    def flyer_preview(self, obj: Show) -> SafeText | str:
        if obj.flyer:
            return format_html('<img src="{}" style="max-height: 50px;" />', obj.flyer.url)
        return "-"
    flyer_preview.short_description = 'Flyer'  # type: ignore[attr-defined]

    def doors_display(self, obj: Show) -> str:
        return obj.doors_at.strftime('%I:%M %p') if obj.doors_at else '-'
    doors_display.short_description = 'Doors'  # type: ignore[attr-defined]
