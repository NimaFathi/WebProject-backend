from rest_framework import serializers
from .models import follow_notification


class notification_serializer(serializers.ModelSerializer):
    class Meta:
        model = follow_notification
        fields = ['follower']

        depth = 1