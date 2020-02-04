from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Channel

# if you need your post you can grab them with card_set (see Post.serializers.py for example)


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class search_channel_serializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('pk', 'name', 'picture')


class channel_user_serializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('pk', 'name', 'picture', 'description')

class channel_view_serializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ('pk', 'name', 'picture', 'description', 'rules', 'followers')