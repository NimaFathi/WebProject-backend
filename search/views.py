from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from Post.models import Card, Comment
from account.models import Account
from Post.serializers import search_card_serializer
from account.serializers import account_search_serializer
from channel.models import Channel
from channel.serializers import search_channel_serializer

@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def search_posts(request):
    query = request.query_params.get('q', None)
    posts = Card.objects.filter(title=query)
    serializer = search_card_serializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def search_users(request):
    query = request.query_params.get('q', None)
    accounts = Account.objects.filter(username=query)
    serializer = account_search_serializer(accounts, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def search_channels(request):
    query = request.query_params.get('q', None)
    channels = Channel.objects.filter(name=query)
    serializer = search_channel_serializer(channels, many=True)
    return Response(serializer.data)




