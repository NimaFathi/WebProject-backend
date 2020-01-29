from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Channel

# if you need your post you can grab them with card_set (see Post.serializers.py for example)
class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'
