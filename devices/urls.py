from django.urls import path
from . import views

app_name = "devices"
urlpatterns = [
    path('home/', views.device, name='device'),
    path('product/<int:product_id>/', views.product, name='product'),
]