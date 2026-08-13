from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    # Main Portal: Targets http://localhost:8000/community/
    path('', views.community_index_view, name='community_index'),
    
    path('post/create/', views.post_create_view, name='post_create'),
    path('post/<int:post_id>/', views.post_detail_view, name='post_detail'),
    path('post/<int:post_id>/comments/', views.comment_list_view, name='comment_list'),
    path('post/<int:post_id>/add-comment/', views.add_comment_view, name='add_comment'),
]
