from django.contrib import admin
from .models import RecommendGame
# Register your models here.

@admin.register(RecommendGame)
class RecommendGameAdnin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'price', 'rank', 'created_at')
    list_filter = ('platform', 'is_free')
    search_fields = ('title', 'description')