from rest_framework import serializers
from .models import Comment, Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'textContent', 'creatorPicture', 'adminId', 'authorId', 'title', 'creatorName', 'pictureContent', 'comment_set', 'voteUp', 'voteDown', )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post','parentId', 'userId', 'username', 'content', 'voteUp', 'voteDown', 'picture', 'time', )   