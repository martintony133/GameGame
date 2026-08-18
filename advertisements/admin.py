from django.contrib import admin
from django.utils.html import format_html
from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'company_name', 'display_media', 'view_website', 'start_date', 'end_date')
    search_fields = ('project_name', 'company_name', 'contact_person')
    list_filter = ('start_date', 'end_date')
    ordering = ('-start_date',)

    def display_media(self, obj):
        if obj.media:
            return format_html('<img src="{}" style="max-height: 40px; border-radius: 4px;" />', obj.media.url)
        return "No media uploaded"
    display_media.short_description = 'Media Preview'

    def view_website(self, obj):
        if obj.company_website:
            return format_html('<a href="{}" target="_blank">Visit Site</a>', obj.company_website)
        return "N/A"
    view_website.short_description = 'Website'
