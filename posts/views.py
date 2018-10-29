from django.shortcuts import render, redirect
from main.models import CustomUser, FriendshipRequest
from posts.models import Post, Comment, LikePost, LikeComment
import datetime


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')

    myUser = CustomUser.objects.get(user=request.user)
    myReqs = FriendshipRequest.objects.filter(user_to=myUser)

    usersList = [myUser] + list(myUser.friends.all())
    postsAll = Post.objects.filter(user__in=usersList).order_by('-date_pub')

    context = {'myUser': myUser, 'myReqs': myReqs, 'postsAll': postsAll}
    return render(request, 'posts/index.html', context)


def post(request):
    if not request.user.is_authenticated:
        return render(request, 'main/login.html')

    myUser = CustomUser.objects.get(user=request.user)    

    text = request.POST.get('text')
    myPost = Post(user=myUser, text=text, date_pub=datetime.datetime.now())
    myPost.save()

    return redirect('post_index')