from django.db import models
from account.models import Account
# Create your models here.


class follow_notification(models.Model):
    follower = models.ManyToManyField(Account, related_name='follower_notif')
    following = models.ManyToManyField(Account, related_name='following_notif')