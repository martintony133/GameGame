from django.urls import path
from . import views

app_name = "accessories"
urlpatterns = [
    path('home/', views.accessory, name='accessory'),
    path('product/<int:product_id>/', views.product, name='product'),
]