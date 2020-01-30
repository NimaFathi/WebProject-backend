from rest_framework import serializers
from .models import Comment, Card


class cardi(serializers.ModelSerializer):
    class Meta:
        model = Card
        field = '__all__'


class CardSerializer(serializers.ModelSerializer):
    creatorPicture = serializers.SerializerMethodField("get_creatorPicture_from_author")
    adminId = serializers.SerializerMethodField("get_adminId_from_channel")
    authorId = serializers.SerializerMethodField("get_authorId_from_author")
    creatorName = serializers.SerializerMethodField("get_creatorName_from_author")

    class Meta:
        model = Card
        fields = (
        'pk', 'textContent', 'creatorPicture', 'adminId', 'author','authorId', 'title', 'creatorName', 'pictureContent',
        'comment_set', 'voteUp', 'voteDown')

    def get_creatorPicture_from_author(self, card):
        creatorPicture = card.author.avatar
        return creatorPicture

    def get_adminId_from_channel(self, card):
        return 1

    def get_authorId_from_author(self, card):
        return card.author.pk

    def get_creatorName_from_author(self, card):
        return card.author.username


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_username_from_author")
    userId = serializers.SerializerMethodField("get_userId_from_author")
    picture = serializers.SerializerMethodField("get_picture_from_author")

    class Meta:
        model = Comment
        fields = ('pk', 'post', 'parentId', 'userId', 'username', 'content', 'voteUp', 'voteDown', 'picture', 'time',)

    def get_username_from_author(self, comment):
        username = comment.author.username
        return username

    def get_userId_from_author(self, comment):
        userId = comment.author.pk
        return userId

    def get_picture_from_author(self, comment):
        picture = comment.author.avatar
        return picture