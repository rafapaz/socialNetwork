from django.db import models
from main.models import CustomUser, user_directory_path


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    date_pub = models.DateTimeField('publish date')
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    def __str__(self):
        return self.user.name + ' -> ' + self.text[:100] + '...'


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    date_pub = models.DateTimeField('publish date')
    text = models.TextField(max_length=512, blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.user.name + ' -> ' + self.text[:100] + '...'


class LikePost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='post_likes')
    like = models.BooleanField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return self.user.name + ' -> ' + str(self.like) + ' -> ' + self.post.text[:100] + '...'


class LikeComment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comment_likes')
    like = models.BooleanField()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')

    def __str__(self):
        return self.user.name + ' -> ' + str(self.like) + ' -> ' + self.comment.text[:100] + '...'