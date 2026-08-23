from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'device','price', 'quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'address', 'paid', 'contact_date']
    list_filter = ['paid', 'contact_date']
    search_fields = ['name', 'email', 'phone']
    list_editable = ['paid']
    inlines = [OrderItemInline]