from rest_framework import serializers
from .models import Comment, Card

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ('id', 'textContent', 'creatorPicture', 'adminId', 'authorId', 'title', 'creatorName', 'pictureContent', 'comment_set', 'voteUp', 'voteDown')

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_username_from_author")
    userId = serializers.SerializerMethodField("get_userId_from_author")
    picture = serializers.SerializerMethodField("get_picture_from_author")

    
    class Meta:
        model = Comment
        fields = ('pk', 'post','parentId', 'userId', 'username', 'content', 'voteUp', 'voteDown', 'picture', 'time', )

    def get_username_from_author(self, comment):
        username = comment.author.username
        return username
    def get_userId_from_author(self, comment):
        usrId = comment.author.pk
        return userId
    def get_picture_from_author(self, comment):
        picture = comment.author.avatar
        return picture   