from django.urls import path
from . import views

app_name = "recommendations"
urlpatterns = [
    path('home/', views.recommendation, name='recommendation'),
]