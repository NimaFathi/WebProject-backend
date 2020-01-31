from Post.models import Comment, Card
from Post.serializers import CardSerializer
from rest_framework.response import Response
from django.db.models import Count
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from account.models import Account


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
    account1 = Account.objects.get(pk=user_id)
    channels = account1.authours.all()
    channel_followings = Card.objects.filter(channel__in=channels)
    people_followings = Card.objects.filter(author__in=account1.following.all())
    try:
        followings = people_followings.union(channel_followings).order_by('date_Modified')
    except people_followings.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CardSerializer(followings, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def contributes(request):
    user_id = request.query_params.get('user_id', None)
    account1 = Account.objects.get(pk=user_id)
    created_posts = Card.objects.filter(author=account1)
    commented_posts = Card.objects.filter(pk__in=Comment.objects.filter(author=account1).values('post'))
    try:
        queryset = commented_posts.union(created_posts).order_by('date_Modified')
    except queryset.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CardSerializer(queryset, many=True)
    return Response(serializer.data)



