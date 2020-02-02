from django.db import models
from account.models import Account
# Create your models here.


class Channel(models.Model):
    picture = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=None , default='images/default_avatar.png')
    admin = models.ForeignKey(Account, null=False, on_delete=models.CASCADE, related_name = 'admin')
    followers = models.ManyToManyField(Account, related_name='authours')
    accounts = models.ManyToManyField(Account, blank=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    rules = models.CharField(max_length=50)

