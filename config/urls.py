"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',include("pages.urls", namespace='pages')),
    path("accounts/", include("accounts.urls", namespace='accounts')),
    path("recommendations/", include("recommendations.urls", namespace='recommendations')),
    path("games/", include("games.urls")),
    path("devices/", include("devices.urls", namespace='devices')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls', namespace='news')),
    path('community/', include('community.urls')),
    path('accessories/', include('accessories.urls')),,
    path('orders/', include('orders.urls', namespace='orders')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "GameGame Admin"
admin.site.site_title = "GameGame Admin Portal"
admin.site.index_title = "Welcome to GameGame Admin Portal"

def global_duplicate_action(modeladmin, request, queryset):
    for obj in queryset:
        original_pk = obj.pk
        obj.pk = None # 清空 ID 讓 Django 知道這是要新增資料
        
        # 自動檢查並在名稱後面加上 _copy
        if hasattr(obj, 'device_name'):
            obj.device_name = f"{obj.device_name}_copy"
        elif hasattr(obj, 'title'):
            obj.title = f"{obj.title}_copy"
        elif hasattr(obj, 'name'):
            obj.name = f"{obj.name}_copy"
            
        obj.save()
        
        # 處理多選欄位（包含 MultiSelectField 同 ManyToManyField）
        original_obj = modeladmin.model.objects.get(pk=original_pk)
        for field in modeladmin.model._meta.get_fields():
            if field.many_to_many or field.one_to_many:
                getattr(obj, field.name).set(getattr(original_obj, field.name).all())
            elif field.__class__.__name__ == 'MultiSelectField':
                setattr(obj, field.name, getattr(original_obj, field.name))
                
        obj.save()

    modeladmin.message_user(request, f"Successfully duplicated {queryset.count()} item(s).")

# 2. 給這個全域動作設定一個在後台下拉選單顯示的名字
global_duplicate_action.short_description = "Duplicate selected items"

# 3. 🔍 關鍵行：向 Django 全站註冊這個功能！
admin.site.add_action(global_duplicate_action)
