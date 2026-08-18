from django.urls import path
from . import views

app_name = "games"
urlpatterns = [
    path('home/', views.game, name='game'),
    path('product/<int:product_id>/', views.product, name='product'),
]