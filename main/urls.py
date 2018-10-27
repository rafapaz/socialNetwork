from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.myLogin, name='login'),
    path('logout/', views.myLogout, name='logout'),
    path('listUsers/', views.listUsers, name='listUsers'),
]
