from django.db import models
from main.models import CustomUser, user_directory_path


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_pub = models.DateTimeField('publish date')
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_pub = models.DateTimeField('publish date')
    text = models.TextField(max_length=512, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class LikePost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    like = models.BooleanField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class LikeComment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    like = models.BooleanField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)