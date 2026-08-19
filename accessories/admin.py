# Accessories/admin.py
from django.contrib import admin
from .models import Accessory, AccessoryColor

class AccessoryColorInline(admin.TabularInline):
    model = AccessoryColor
    extra = 1  # Shows 1 empty slot by default to quickly add a new color
    fields = ('color_name', 'color_code')

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    # Adjust 'accessory_name' if your model field has a different name
    list_display = ('accessory_name', 'get_colors_count')
    
    # Embeds the color inline table directly inside the Accessory page
    inlines = [AccessoryColorInline]

    # Custom column to show the total number of colors for this accessory
    def get_colors_count(self, obj):
        return obj.colors.count()
    get_colors_count.short_description = 'Available Colors Count'
