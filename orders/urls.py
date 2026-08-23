from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('cart/', views.order_create, name='order_create'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('delete/<int:order_id>/', views.order_delete, name='order_delete'),
    path('checkout/', views.checkout, name='checkout'),
]