from django.db import models
from account.models import Account
# Create your models here.


class Card(models.Model):
    id = models.IntegerField(primary_key=True , default=1)
    textContent = models.TextField()
    author = models.ForeignKey(Account,on_delete=models.CASCADE, related_name = 'card_author', default = None)
    title = models.CharField(max_length=100)
    pictureContent = models.FileField(upload_to='images')
    voteUp = models.ManyToManyField(Account , blank=True)
    voteDown = models.ManyToManyField(Account, related_name='voteDown', blank=True)
    date_Modified = models.DateTimeField(auto_now_add=True)
    

class Comment(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    post = models.ForeignKey(Card, on_delete=models.CASCADE)
    parentId = models.IntegerField(null=True)
    author = models.ForeignKey(Account,on_delete=models.CASCADE, related_name = 'comment_authour', default = None)
    content = models.TextField()
    voteUp = models.ManyToManyField(Account,related_name='voteUp', blank=True)
    voteDown = models.ManyToManyField(Account, blank=True)
    picture = models.FileField(upload_to='images')
    time = models.DateField(auto_now_add=True)
