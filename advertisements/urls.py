from django.urls import path
from . import views

urlpatterns = [
    # 確保 recommendations/home/ 呢個網址係指向你啱啱寫嘅 views.home_view
    path('recommendations/home/', views.home_view, name='home'),
]
