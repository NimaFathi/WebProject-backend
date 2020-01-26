from .serializers import ChannelSerializer
from rest_framework import viewsets
from .models import channel


class channel_detail(viewsets.ModelViewSet):
    queryset = channel.objects.all()
    serializer_class = ChannelSerializer
