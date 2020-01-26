from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user_id','user_name', 'avatar', 'user_email', 'occupy', 'bio']
