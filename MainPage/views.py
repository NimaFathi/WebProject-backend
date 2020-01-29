from django.shortcuts import render
from rest_framework import viewsets
from Post.models import Comment, Card
from Post.serializers import CommentSerializer, CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

class hottest(viewsets.ModelViewSet):
    queryset = Card.objects.annotate(q_count=Count('voteUp')).order_by('-q_count')[:10]
    serializer_class = CardSerializer

class newest(viewsets.ModelViewSet):
    serializer_class = CardSerializer
    queryset = Card.objects.all().order_by('date_Modified')