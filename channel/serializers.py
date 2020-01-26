from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import channel


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = channel
        fields = '__all__'
