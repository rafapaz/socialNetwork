from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class CustomUser(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    nasc_date = models.DateField('birth date')
    img_profile = models.ImageField(upload_to=user_directory_path, default = 'avatar2.png')

    friends = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name

class FriendshipRequest(models.Model):
    user_from = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')
    user_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')
    send_date = models.DateTimeField('send date')

    def __str__(self):
        return self.user_from.name + ' to ' + self.user_to.name