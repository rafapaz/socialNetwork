from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='post_index'),
    path('post/', views.post, name='post'),
    path('post/like/<int:post_id>', views.post_like, name='post_like'),
]