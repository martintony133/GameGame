from django.contrib import admin
from django.utils import timezone
from .models import Product, FestivalSale, FestivalSaleItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_type', 'product_name', 'price')
    list_filter = ('product_type',)

class FestivalSaleItemInline(admin.TabularInline):
    model = FestivalSaleItem
    extra = 1 
    raw_id_fields = ('product',) 

@admin.register(FestivalSale)
class FestivalSaleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'start_date', 
        'end_date', 
        'display_current_status',   
        'updated_at'             
    )
    
    list_filter = ('title', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    inlines = [FestivalSaleItemInline]
    readonly_fields = ('display_current_status', 'updated_at')

    def display_current_status(self, obj):
        if not obj or not obj.start_date or not obj.end_date:
            return '-'

        now = timezone.now()
        if obj.start_date <= now <= obj.end_date:
            return '🟢 Live'
        elif now < obj.start_date:
            return '🟡 UpComing'
        else:
            return '🔴 Expired'
            
    display_current_status.short_description = 'Status'