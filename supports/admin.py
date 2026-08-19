from django.contrib import admin
from .models import SupportTicket

@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'name', 'email', 'is_resolved', 'created_at')
    
    list_filter = ('is_resolved', 'created_at')
    
    search_fields = ('name', 'email', 'subject', 'message')
    

    list_editable = ('is_resolved',)
