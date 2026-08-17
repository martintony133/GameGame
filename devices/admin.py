from django.contrib import admin
from import_export.admin import ImportExportModelAdmin # 如果你有用 import_export 嘅話
from .models import Device
from django import forms

# 1. 建立一個 Custom Form，將 color_code 綁定 HTML5 嘅顏色條 (Color Picker)
class DeviceAdminForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'
        widgets = {
            'color_code': forms.TextInput(attrs={'type': 'color', 'style': 'width: 100px; height: 40px; cursor: pointer;'}),
        }

# 2. 註冊 Device 到 Admin 後台
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    form = DeviceAdminForm
    # 喺列表畫面顯示名、類型同埋顏色代碼
    list_display = ('device_name', 'device_type', 'color_code') 
