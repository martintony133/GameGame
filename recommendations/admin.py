from django.contrib import admin
from .models import RecommendedGame
# Register your models here.

@admin.register(RecommendedGame)
class RecommendedGameAdnin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'price', 'rank', 'created_at')
    list_filter = ('platform', 'is_free')
    search_fields = ('title', 'description')