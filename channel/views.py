from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from channel.models import Channel
from rest_framework import status
from .serializers import ChannelSerializer, channel_view_serializer
from Post.models import Card
from Post.serializers import search_card_serializer, CardSerializer
from account.serializers import account_search_serializer
from account.models import Account
from channel.serializers import channel_user_serializer, get_followers_serializer
from copy import copy

# @api_view(['POST', ])
# # @permission_classes([IsAuthenticated, ])
# def create_channel(request):
#     serializer = ChannelSerializer(data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


@api_view(['POST', ])
@permission_classes([IsAuthenticated,])
def create_channel(request):
    serializer = ChannelSerializer(data=request.data, partial=True)
    if serializer.is_valid():
        channel = serializer.save()
        ser = ChannelSerializer(channel)
    return Response(ser.data)


@api_view(['PUT', ])
@permission_classes([IsAuthenticated, ])
def edit_channel(request):
    channel_id = request.data['channel_id']
    try:
        channel = Channel.objects.get(pk=channel_id)
    except Channel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    channel_authors = copy(channel.accounts.all())
    serializer = ChannelSerializer(channel, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    channel.accounts.add(*channel_authors)
    return Response(serializer.data)


@api_view(['DELETE', ])
def remove_author(request):
    channel_id = request.data['channel_id']
    user_id = request.data['user_id']
    user = Account.objects.get(pk=user_id)
    channel = Channel.objects.get(pk=channel_id)
    channel.accounts.remove(user)
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST', ])
def add_follower(request):
    channel_id = request.data['channel_id']
    user_id = request.data['user_id']
    channel = Channel.objects.get(pk=channel_id)
    user = Account.objects.get(pk=user_id)
    channel.followers.add(user)
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE', ])
def remove_follower(request):
    channel_id = request.data['channel_id']
    user_id = request.data['user_id']
    channel = Channel.objects.get(pk=channel_id)
    user = Account.objects.get(pk=user_id)
    channel.followers.remove(user)
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET', ])
def channel_view(request):
    channel_id = request.query_params.get('channel_id', None)
    try:
        channel = Channel.objects.get(pk=channel_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    channels_posts = Card.objects.filter(channel=channel)
    posts_serializer = CardSerializer(channels_posts, many=True)
    channel_serializer = channel_view_serializer(channel)
    admin_serializer = account_search_serializer(channel.admin)
    authors = channel.accounts.all()
    authors_serializer = account_search_serializer(authors, many=True)
    return Response([channel_serializer.data, admin_serializer.data, authors_serializer.data, posts_serializer.data])


@api_view(['GET'])
def user_channels(request):
    user_id = request.query_params.get('user_id', None)
    try:
        account = Account.objects.get(pk=user_id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user_channels = Channel.objects.filter(admin=account)
    serializer = channel_user_serializer(user_channels, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def get_followers(request):
    channel_id = request.query_params.get('channel_id', None)
    channel = Channel.objects.get(pk=channel_id)
    followers_serializer = get_followers_serializer(channel)
    return Response(followers_serializer.data)