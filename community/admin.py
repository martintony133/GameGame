from django.contrib import admin
from .models import CommunityCategory, CommunityPost, CommunityComment

# Register your models here so they appear in Django Admin
admin.site.register(CommunityCategory)
admin.site.register(CommunityPost)
admin.site.register(CommunityComment)
