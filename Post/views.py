from django.shortcuts import render
from rest_framework import viewsets
from .models import Comment, Card
from .serializers import CommentSerializer, CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

SUCCESS = 'success'
ERROR = 'error'
DELETE_SUCCESS = 'deleted'
UPDATE_SUCCESS = 'updated'
CREATE_SUCCESS = 'created'


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def detail_card_view(request, id):
    try:
        card = Card.objects.get(id=id)
    except Card.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CardSerializer(card)
        return Response(serializer.data)


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def detail_comment_view(request, id):
    try:
        comment = Comment.objects.get(id=id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def update_card_view(request, id):
    try:
        card = Card.objects.get(id=id)
    except Card.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if card.author != user:
        return Response({'response': "you don't have permission to edit."})

    if request.method == 'PUT':
        serializer = CardSerializer(card, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = UPDATE_SUCCESS
            data['pk'] = card.pk
            if card.channel != null:
                data['adminId'] = card.channel.admin.pk
            else:
                data['adminId'] = null
            data['userId'] = card.author.pk
            data['textcontent'] = card.content
            data['voteDown'] = card.voteDown
            data['voteUp'] = card.voteUp
            data['comments'] = card.comment_set
            image_url = str(request.build_absolute_uri(card.pictureContent.url))
            if "?" in image_url:
                image_url = image_url[:image_url.rfind("?")]
            data['pictureContent'] = image_url
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def update_comment_view(request, id):
    try:
        comment = Comment.objects.get(id=id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if comment.author != user:
        return Response({'response': "you don't have permission to edit."})

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = UPDATE_SUCCESS
            data['pk'] = comment.pk
            data['parentId'] = comment.parentId
            data['userId'] = comment.author.pk
            data['username'] = comment.author.username
            data['content'] = comment.content
            data['voteDown'] = comment.voteDown
            data['voteUp'] = comment.voteUp
            image_url = str(request.build_absolute_uri(comment.author.avatar.url))
            if "?" in image_url:
                image_url = image_url[:image_url.rfind("?")]
            data['picture'] = image_url
            data['time'] = comment.time
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def is_author_of_card(request, id):

    try:
        card = Card.objects.get(pk=id)
    except Card.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = {}
    user = request.user
    if card.author != user:
        data['response'] = "you don't have permission to edit"
        return Response(data=data)
    data['response'] = "You have permission to edit."
    return Response(data=data)


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def is_author_of_comment(request, id):
    try:
        comment = Comment.objects.get(pk=id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = {}
    user = request.user
    if comment.author != user:
        data['response'] = "you don't have permission to edit"
        return Response(data=data)
    data['response'] = "You have permission to edit."
    return Response(data=data)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def delete_card_view(request, id):
    try:
        card = Card.objects.get(pk=id)
    except Card.DoesNotExist:
        return Response({'response': "You don't have permission to delete."})

    if request.method == "DELETE":
        operation = card.delete()
        data = {}
        if operation:
            data['response'] = DELETE_SUCCESS
            return Response(data=data)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def delete_comment_view(request, id):
    try:
        comment = Comment.objects.get(pk=id)
    except Comment.DoesNotExist:
        return Response({'response': "You don't have permission to delete."})

    if request.methode == "DELETE":
        operation = comment.delete()
        data = {}
        if operation:
            data['response'] = DELETE_SUCCESS
            return Response(data=data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def create_card_view(request):
    if request.method == 'POST':
        data = request.data
        data['author'] = request.user.pk
        serializer = CardSerializer(data=data)
        data = {}
        if serializer.is_valid():
            card = serializer.save()
            data['response'] = CREATE_SUCCESS
            data['pk'] = card.pk
            if card.channel is not None:
                data['adminId'] = card.channel.admin.pk
            data['userId'] = card.author.pk
            data['textcontent'] = card.textContent
            data['voteDown'] = card.voteDown.all()
            data['voteUp'] = card.voteUp.all()
            data['comments'] = card.comment_set.all()
            image_url = str(request.build_absolute_uri(card.pictureContent.url))
            if "?" in image_url:
                image_url = image_url[:image_url.rfind("?")]
            image_url = image_url.encode('utf-8').strip()
            data['pictureContent'] = image_url
            data['creatorPicture'] = card.author.avatar
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def create_comment_view(request):
    if request.method == 'POST':
        data = request.data
        data['author'] = request.user.pk
        serializer = CommentSerializer(data=data)

        data = {}
        if serializer.is_valid():
            comment = serializer.save()
            data['response'] = CREATE_SUCCESS
            data['pk'] = comment.pk
            data['parentId'] = comment.parentId
            data['userId'] = comment.author.pk
            data['username'] = comment.author.username
            data['content'] = comment.content
            data['voteDown'] = comment.voteDown.all()
            data['voteUp'] = comment.voteUp.all()
            image_url = str(request.build_absolute_uri(comment.author.avatar.url))
            if "?" in image_url:
                image_url = image_url[:image_url.rfind("?")]
            data['picture'] = image_url
            data['time'] = comment.time.encode
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
