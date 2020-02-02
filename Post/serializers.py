from rest_framework import serializers
from .models import Comment, Card
from account.serializers import AccountPropertiesSerializer
from django.http import JsonResponse

class search_card_serializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('pk', 'title', 'pictureContent')


class CardSerializer(serializers.ModelSerializer):
    adminId = serializers.SerializerMethodField("get_adminId_from_channel")
    authorId = serializers.SerializerMethodField("get_authorId_from_author")
    creatorName = serializers.SerializerMethodField("get_creatorName_from_author")
    profilePicture = serializers.SerializerMethodField("get_creatorPicture_from_author")

    class Meta:
        model = Card
        fields = (
        'pk', 'textContent', 'adminId', 'author','authorId', 'title', 'creatorName' , 'profilePicture',
        'comment_set', 'voteUp', 'voteDown', 'pictureContent')

    def get_creatorPicture_from_author(self, card):
        creatorPicture = str(card.author.avatar)
        return creatorPicture

    def get_adminId_from_channel(self, card):
        if card.channel is not None:
            queryset     = card.channel.admin.pk
            print(queryset)
            return queryset
        else:
            return None

    def get_authorId_from_author(self, card):
            return card.author.pk

    def get_creatorName_from_author(self, card):
        return card.author.username


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_username_from_author")
    userId = serializers.SerializerMethodField("get_userId_from_author")
    profilePicture = serializers.SerializerMethodField("get_creatorPicture_from_author")


    class Meta:
        model = Comment
        fields = ('pk', 'post','author' ,'parentId', 'userId', 'username','content','profilePicture', 'voteUp', 'voteDown', 'time',)

    def get_username_from_author(self, comment):
        username = comment.author.username
        return username

    def get_userId_from_author(self, comment):
        userId = comment.author.pk
        return userId

    def get_creatorPicture_from_author(self, comment):
        creatorPicture = str(comment.author.avatar)
        return creatorPicture