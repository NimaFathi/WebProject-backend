from django.shortcuts import render
from rest_framework import viewsets
from .models import Comment, Card
from .serializers import CommentSerializer, CardSerializer

class CardView(viewsets.ModelViewSet):
    queryset = Card.objects.all() 
    serializer_class = CardSerializer

class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



