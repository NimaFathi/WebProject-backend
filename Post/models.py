from django.db import models
from account.models import Account
from channel.models import Channel
from versatileimagefield.fields import VersatileImageField ,PPOIField

class Card(models.Model):
    textContent = models.TextField()
    author = models.ForeignKey(Account , null=False , on_delete=models.CASCADE, related_name='card_author')
    channel = models.ForeignKey(Channel , blank=True , null=True, on_delete=models.CASCADE, related_name='for_channel')
    title = models.CharField(max_length=100)
    pictureContent = VersatileImageField('pictureContent', upload_to='images' , default='images/default_avatar.png' )
    voteUp = models.ManyToManyField(Account , blank=True)
    voteDown = models.ManyToManyField(Account, related_name='voteDown', blank=True)
    date_Modified = models.DateTimeField(auto_now_add=True)
    

class Comment(models.Model):
    post = models.ForeignKey(Card, on_delete=models.CASCADE)
    parentId = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Account,on_delete=models.CASCADE, related_name = 'comment_authour', default=None)
    content = models.TextField()
    voteUp = models.ManyToManyField(Account,related_name='voteUp', blank=True)
    voteDown = models.ManyToManyField(Account, blank=True)
    time = models.DateField(auto_now_add=True, null=True)
    is_seen = models.IntegerField(default=0)
