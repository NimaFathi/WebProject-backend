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

class hottest(viewsets.ModelViewSet):
    queryset = Card.objects.annotate(q_count=Count('voteUp')).order_by('-q_count')[:10]
    serializer_class = CardSerializer

class newest(viewsets.ModelViewSet):
    queryset = Card.objects.all().order_by('date_Modified')[:10]
    serializer_class = CardSerializer
