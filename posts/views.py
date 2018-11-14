from django.shortcuts import render, redirect, get_object_or_404
from main.models import CustomUser, FriendshipRequest
from posts.models import Post, Comment, LikePost, LikeComment
import datetime


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    myUser = CustomUser.objects.get(user=request.user)
    myReqs = FriendshipRequest.objects.filter(user_to=myUser)

    usersList = [myUser] + list(myUser.friends.all())
    postsAll = Post.objects.filter(user__in=usersList).order_by('-date_pub')

    context = {'myUser': myUser, 'myReqs': myReqs, 'postsAll': postsAll}
    return render(request, 'posts/index.html', context)


def post(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST" and request.POST.get('text') != '':
        myUser = CustomUser.objects.get(user=request.user)
        text = request.POST.get('text')
        myPost = Post(user=myUser, text=text, date_pub=datetime.datetime.now())
        myPost.save()

    return redirect('post_index')


def post_like(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')

    post = get_object_or_404(Post, pk=post_id)
    myUser = CustomUser.objects.get(user=request.user)
    likes = LikePost.objects.filter(post=post, user=myUser)
    if not likes:
        like = LikePost()
        like.like = True
        like.post = post
        like.user = myUser
        like.save()
    else:
        like = likes[0]
        like.delete()

    return redirect('post_index')


def post_comment(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST" and request.POST.get('comment') != '':
        post = get_object_or_404(Post, pk=post_id)
        myUser = CustomUser.objects.get(user=request.user)

        com = Comment()
        com.post = post
        com.user = myUser
        com.date_pub = datetime.datetime.now()
        com.text = request.POST.get('comment')
        com.save()

    return redirect('post_index')


def post_share(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')

    post = get_object_or_404(Post, pk=post_id)
    myUser = CustomUser.objects.get(user=request.user)

    newPost = Post()
    newPost.user = myUser
    newPost.date_pub = datetime.datetime.now()
    newPost.repost = True
    newPost.original_user = post.user
    newPost.text = post.text
    newPost.image = post.image
    newPost.save()

    return redirect('post_index')
