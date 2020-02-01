from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from channel.models import Channel
from rest_framework import status
from .serializers import ChannelSerializer


@api_view(['POST', ])
@permission_classes([IsAuthenticated, ])
def create_channel(request):
    serializer = ChannelSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT', ])
@permission_classes([IsAuthenticated, ])
def edit_channel(request):
    channel_id = request.query_params.get('channel_id', None)
    try:
        channel = Channel.objects.get(pk=channel_id)
    except Channel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.user != channel.admin:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)

    serializer = ChannelSerializer(channel, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(channel.name)



