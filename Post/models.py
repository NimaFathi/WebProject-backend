from django.db import models
from django.contrib.auth.models import User 
from UserProfile.models import UserProfile
# Create your models here.


class Card(models.Model):
    id = models.IntegerField(primary_key=True , default=1)
    textContent = models.TextField()
    creatorPicture = models.FileField(upload_to='images')
    adminId = models.IntegerField(blank=False , null=False)
    authorId = models.IntegerField(blank=False , null=False)
    title = models.CharField(max_length=100)
    creatorName = models.CharField(max_length=50)
    pictureContent = models.FileField(upload_to='images')
    voteUp = models.ManyToManyField(UserProfile , blank=True)
    voteDown = models.ManyToManyField(UserProfile, related_name='voteDown', blank=True)
    date_Modified = models.DateTimeField(auto_now_add=True)
    

class Comment(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    post = models.ForeignKey(Card, on_delete=models.CASCADE)
    parentId = models.IntegerField(null=True)
    userId = models.IntegerField(null=False, blank=False)
    username = models.CharField(max_length=50)
    content = models.TextField()
    voteUp = models.ManyToManyField(UserProfile,related_name='voteUp', blank=True)
    voteDown = models.ManyToManyField(UserProfile, blank=True)
    picture = models.FileField(upload_to='images')
    time = models.DateField(auto_now_add=True)
