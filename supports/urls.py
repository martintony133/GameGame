from django.urls import path
from . import views
app_name = "supports"

urlpatterns = [
    path('report/', views.support_create_view, name='report'),
]
