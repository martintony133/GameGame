from django.urls import path
from . import views

app_name = 'promotions'
urlpatterns = [
    path('game/', views.promo_game, name='promo_game'),
    path('discount_page/<int:pk>/', views.discount_page, name='discount_page')
]