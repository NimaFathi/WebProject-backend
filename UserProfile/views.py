from rest_framework import viewsets
from account.models import Account
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import Account
from rest_framework import generics, status
from account.serializers import user_profile_serializer, profile_serializer
from account.serializers import ProfileSerializer, change_profile_serializer
from rest_framework.decorators import api_view
from notifications.models import follow_notification
from Post.serializers import CardSerializer
from Post.models import Card
from notifications.serializer import notification_serializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated




class change_profile(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        user_id = request.data['user_id']
        account1 = Account.objects.get(pk=user_id)
        serializer = change_profile_serializer(account1, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def user_profile(request):
    user_id = request.query_params['user_id']
    account = Account.objects.get(pk=user_id)

    account_posts = Card.objects.filter(author=account, channel=None)
    posts_serializer = CardSerializer(account_posts, many=True)

    profile_serializer = user_profile_serializer(account)

    following_accounts = follow_notification.objects.filter(follower=account).values('following_id')
    following_accounts = Account.objects.filter(pk__in=following_accounts)
    following_serializer = user_profile_serializer(following_accounts, many=True)

    follower_accounts = follow_notification.objects.filter(following=account).values('follower_id')
    follower_accounts = Account.objects.filter(pk__in=follower_accounts)
    follower_serializer = user_profile_serializer(follower_accounts, many=True)

    return Response([profile_serializer.data, posts_serializer.data, following_serializer.data, follower_serializer.data])


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def get_followers(request):
    user_id = request.query_params['user_id']
    account = Account.objects.get(pk=user_id)
    followers = follow_notification.objects.filter(following=account)
    serializer = notification_serializer(followers, many=True)
    return Response(serializer.data)