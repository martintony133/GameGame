from django.contrib import admin
from .models import Genre
# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'price', 'stars')
    list_display_links = ('title',)
    list_filter = ('platform', 'stars')
    search_fields = ('title',)
    list_per_page = 20
    fieldsets = [
        ('Information',{'fields': ('title', 'platform', 'price', 'stars')}),
        ('Main Photo',{'fields':('photo_main',)}),
        ('Other Photo',{'classes':('collapse',),
        'fields':('photo_1','photo_2','photo_3','photo_4','photo_5','photo_6')})
    ]