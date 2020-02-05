from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from Post.models import Card, Comment
from account.models import Account
from .models import follow_notification
from Post.serializers import CommentSerializer
from account.serializers import AccountPropertiesSerializer
from copy import copy
# Create your views here.


@api_view(['GET', ])
# @permission_classes([IsAuthenticated, ])
def follow_notifications(request):
    user_id = request.query_params.get('user_id', None)
    user_account = Account.objects.get(pk=user_id)
    new_followings_accounts = copy(follow_notification.objects.filter(following=user_account).values('follower'))
    follow_notification.objects.filter(following=user_account).delete()
    serializer = AccountPropertiesSerializer(new_followings_accounts, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
# @permission_classes([IsAuthenticated, ])
def comment_notifications(request):
    user_id = request.query_params.get('user_id', None)
    new_comments = copy(Comment.objects.filter(is_seen=0, post__author__id=user_id))
    Comment.objects.filter(is_seen=0, post__author__id=user_id).update(is_seen=1)
    serializer = CommentSerializer(new_comments, many=True)
    return Response(serializer.data)
