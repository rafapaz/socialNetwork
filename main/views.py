from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')

    myUser = CustomUser.objects.get(user=request.user)
    context = {'myUser': myUser}
    return render(request, 'main/index.html', context)
    
        