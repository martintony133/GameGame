from django.urls import path
from . import views
app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('faq', views.faq, name='faq'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
]