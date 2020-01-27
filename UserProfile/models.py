from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    avatar = models.ImageField(default='path/to/my/default/image.jpg')
    user_email = models.EmailField()
    occupy = models.CharField(max_length=20)
    bio = models.CharField(max_length=50)