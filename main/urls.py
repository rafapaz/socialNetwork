from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.myLogin, name='login'),
    path('logout/', views.myLogout, name='logout'),
    path('listUsers/', views.listUsers, name='listUsers'),
    path('requestFriend/', views.requestFriend, name='requestFriend'),
    path('listAccept/', views.listAccept, name='listAccept'),
    path('acceptFriend/', views.acceptFriend, name='acceptFriend'),
    path('<int:user_id>/', views.profile, name='profile'),
]
