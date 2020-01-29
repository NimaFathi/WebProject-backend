from django.shortcuts import render
from rest_framework import viewsets
from .models import Comment, Card
from .serializers import CommentSerializer, CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
class CardView(viewsets.ModelViewSet):
    queryset = Card.objects.all() 
    serializer_class = CardSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer