from django.db import models

class Account(models.Model):
    email = models.EmailField(verbose_name='email', max_length=50, unique=True)
    username = models.CharField(max_length=40, unique=True)
    password =  models.CharField()
    def __str__(self):
        return self.email


