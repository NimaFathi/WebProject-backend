from .serializers import ChannelSerializer
from rest_framework import viewsets
from .models import Channel


class channel_detail(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
