from django.shortcuts import render
from rest_framework import viewsets
from .models import Comment, Card
from .serializers import CommentSerializer, CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
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
        data = serializer.data
        if card.channel != None:
            data['profilePicture'] = card.channel.picture.url
        return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def detail_comment_view(request, id):
    try:
        comment = Comment.objects.get(id=id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(data=serializer.data,status=status.HTTP_200_OK)



@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def update_card_view(request, id):
    flag = 0
    try:
        card = Card.objects.get(id=id)
    except Card.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if card.channel != None:
        my_list = list(card.channel.accounts.all())
        for x in my_list:
            if request.user == x:
                flag += 1
                break
        if request.user == card.channel.admin:
            flag += 1
        if request.user == card.author:
            flag += 1
        if flag == 0:
             return Response({'response': "you don't have permission to edit."}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        data = request.data
        serializer = CardSerializer(card, data=data, partial=True)
        if serializer.is_valid():
            if 'voteUp' not in request.data:
                serializer.validated_data['voteUp'] = []
            if 'voteDown' not in request.data:
                serializer.validated_data['voteDown'] = []
            serializer.save()
            data = serializer.data
            data['response'] = UPDATE_SUCCESS
            print(serializer.data)
            return Response(data=data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def update_comment_view(request, id):
    try:
        comment = Comment.objects.get(id=id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if comment.author != user:
         return Response({'response': "you don't have permission to edit."}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        data = {}
        if serializer.is_valid():
            serializer.save()
            if 'voteUp' not in request.data:
                serializer.validated_data['voteUp'] = []
            if 'voteDown' not in request.data:
                serializer.validated_data['voteDown'] = []
            serializer.save()
            data = serializer.data
            data['response'] = UPDATE_SUCCESS
            return Response(data=data, status=status.HTTP_200_OK)
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
        return Response(data=data, status=status.HTTP_403_FORBIDDEN)
    data['response'] = "You have permission to edit."
    return Response(data=data,status=status.HTTP_200_OK)


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
        return Response(data=data,status=status.HTTP_403_FORBIDDEN)
    data['response'] = "You have permission to edit."
    return Response(data=data,status=status.HTTP_200_OK)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def delete_card_view(request, id):
    try:
        card = Card.objects.get(pk=id)
    except Card.DoesNotExist:
        return Response({'response': "You don't have permission to delete."},status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = card.delete()
        data = {}
        if operation:
            data['response'] = DELETE_SUCCESS
            return Response(data=data,status=status.HTTP_200_OK)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def delete_comment_view(request, id):
    try:
        comment = Comment.objects.get(pk=id)
    except Comment.DoesNotExist:
        return Response(data={'response': "You don't have permission to delete."},status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = comment.delete()
        data = {}
        if operation:
            data['response'] = DELETE_SUCCESS
            return Response(data=data,status=status.HTTP_200_OK)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def create_card_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = CardSerializer(data=data)
        data = {}
        if serializer.is_valid():
            card = serializer.save()
            ser = CardSerializer(card)
            data = ser.data
            data['response'] = CREATE_SUCCESS
            if card.channel != None:
                data['profilePicture'] = card.channel.picture.url
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def create_comment_view(request):
    if request.method == 'POST':
        data = request.data
        serializer = CommentSerializer(data=data)

        data = {}
        if serializer.is_valid():
            comment = serializer.save()
            ser = CommentSerializer(comment)
            return Response(data=ser.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

