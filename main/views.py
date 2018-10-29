from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser, FriendshipRequest
from django.contrib.auth import authenticate, login, logout
import datetime


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')

    myUser = CustomUser.objects.get(user=request.user)
    myReqs = FriendshipRequest.objects.filter(user_to=myUser)
        
    context = {'myUser': myUser, 'otherUser': myUser, 'myReqs': myReqs}
    return render(request, 'main/index.html', context)
    
def profile(request, user_id):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')

    myUser = CustomUser.objects.get(user=request.user)
    otherUser = CustomUser.objects.get(pk=user_id)
    myReqs = FriendshipRequest.objects.filter(user_to=myUser)
        
    context = {'myUser': myUser, 'otherUser': otherUser, 'myReqs': myReqs}
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
        return redirect('index')        
    except:
        context = {'message': 'Email or password not valid'}
        return render(request, 'main/login.html', context)
    
def myLogout(request):
    logout(request)
    return render(request, 'main/login.html')

def listUsers(request):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')

    keyword = request.POST.get('keyword')
    if keyword is None:
        keyword = ''
    else:
        request.session['keyword'] = keyword

    myUser = CustomUser.objects.get(user=request.user)    
    
    usersList = CustomUser.objects.filter(name__icontains=request.session['keyword'])
    usersList = list(set(usersList) - set([myUser]))

    friendshipReqs = FriendshipRequest.objects.filter(user_from=myUser)
    usersReqList = []
    for f in friendshipReqs:
        usersReqList.append(f.user_to)

    myReqs = FriendshipRequest.objects.filter(user_to=myUser)
    
    context = {'usersList': usersList, 'myUser': myUser, 'usersReqList': usersReqList, 'myReqs':myReqs}
    return render(request, 'main/listUsers.html', context)

def requestFriend(request):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')

    myUser = CustomUser.objects.get(user=request.user)
    toUser = CustomUser.objects.get(pk=request.POST.get('id'))

    reqFriend = FriendshipRequest(user_from=myUser, user_to=toUser, send_date=datetime.datetime.now())
    reqFriend.save()

    if request.POST.get('list') is not None:
        return redirect('listUsers')
    
    return redirect('index')

def listAccept(request):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')

    myUser = CustomUser.objects.get(user=request.user)
    myReqs = FriendshipRequest.objects.filter(user_to=myUser)
        
    context = {'myUser': myUser, 'myReqs': myReqs}
    return render(request, 'main/listAccept.html', context)

def acceptFriend(request):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')

    myUser = CustomUser.objects.get(user=request.user)
    fromUser = CustomUser.objects.get(pk=request.POST.get('user_id'))

    myUser.friends.add(fromUser)
    myUser.save()

    reqs = FriendshipRequest.objects.filter(user_from=fromUser,user_to=myUser) | FriendshipRequest.objects.filter(user_from=myUser,user_to=fromUser)
    reqs.delete()

    if request.POST.get('list') is not None:
        return redirect('listAccept')
    
    return redirect('index')