from rest_framework import serializers
from .models import Account

from django.contrib.auth.hashers import make_password


class account_search_serializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'pk', 'avatar')


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(RegistrationSerializer, self).create(validated_data)


    

class AccountPropertiesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = ['pk', 'email', 'username','following', 'avatar' ]


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'occupy', 'bio', 'card_set']




class ChangePasswordSerializer(serializers.Serializer):

	old_password 				= serializers.CharField(required=True)
	new_password 				= serializers.CharField(required=True)
	confirm_new_password 		= serializers.CharField(required=True)


class SocialSerializer(serializers.Serializer):
    
    provider = serializers.CharField(max_length=255, required=True)
    access_token = serializers.CharField(max_length=4096, required=True, trim_whitespace=True)