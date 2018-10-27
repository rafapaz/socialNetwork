from django.contrib import admin

from .models import CustomUser, FriendshipRequest

admin.site.register(CustomUser)
admin.site.register(FriendshipRequest)
