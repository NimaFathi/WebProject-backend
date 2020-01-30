from django.shortcuts import render
from rest_framework import viewsets
from Post.models import Comment, Card
from Post.serializers import CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from account.models import Account
from channel.models import Channel
from channel.serializers import ChannelSerializer


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def hottest(request):
    try:
        queryset = Card.objects.annotate(q_count=Count('voteUp')).order_by('-q_count')[:10]
    except queryset.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CardSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def newest(request):
    try:
        queryset = Card.objects.all().order_by('date_Modified')[:10]
    except queryset.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CardSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def following(request):
    user_id = request.query_params.get('user_id', None)
    account1 = Account.objects.filter(pk=user_id)
    channels = account1.channels.all()
    serializer = ChannelSerializer(channels, many=True)
    return Response(serializer)

@api_view()




