from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')

    myUser = CustomUser.objects.get(user=request.user)
    context = {'myUser': myUser}
    return render(request, 'main/index.html', context)
    
def myLogin(request):
    try:
        email = request.POST.get('email')
        psw = request.POST.get('psw')
        myUser = CustomUser.objects.get(email=email)
        sysUser = authenticate(username=myUser.user.username, password=psw)

        if sysUser is None:
            raise Exception('Shit!')

        login(request, sysUser)
        context = {'myUser': myUser}
        return render(request, 'main/index.html', context)        
    except:
        context = {'message': 'Email or password not valid'}
        return render(request, 'main/login.html', context)
    
def myLogout(request):
    logout(request)
    return render(request, 'main/login.html')

def listUsers(request):
    keyword = request.POST.get('keyword')
    if keyword is None:
        keyword = ''
        
    usersList = CustomUser.objects.filter(name__icontains=keyword)
    context = {'usersList': usersList}
    return render(request, 'main/listUsers.html', context)