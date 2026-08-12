from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news, name='home'),
    path('home', views.news, name='home'),
    path('post', views.post, name='post'),

]