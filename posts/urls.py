from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='post_index'),
    path('post/', views.post, name='post'),
    path('post/like/<int:post_id>', views.post_like, name='post_like'),
    path('post/comment/<int:post_id>', views.post_comment, name='post_comment'),
    path('post/share/<int:post_id>', views.post_share, name='post_share'),
]