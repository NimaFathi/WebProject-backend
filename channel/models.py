from django.db import models
from Post.models import Card
from UserProfile.models import UserProfile
# Create your models here.

class channel(models.Model):
    picture = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    admin = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name = 'admin')
    authours = models.ManyToManyField(UserProfile, related_name = 'authors')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    rules = models.CharField(max_length=50)
    posts = models.ManyToManyField(Card)
