from django.db import models
from account.models import Account
# Create your models here.


class follow_notification(models.Model):
    follower = models.ForeignKey(Account, related_name='follower_notif', on_delete=models.CASCADE)
    following = models.ForeignKey(Account, related_name='following_notif', on_delete=models.CASCADE)
    is_used = models.IntegerField(default=0)