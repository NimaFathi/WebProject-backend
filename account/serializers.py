from rest_framework import serializers
from .models import Account

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    

class AccountPropertiesSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = ['pk', 'email', 'username', ]


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'occupy', 'bio', 'card_set']




class ChangePasswordSerializer(serializers.Serializer):

	old_password 				= serializers.CharField(required=True)
	new_password 				= serializers.CharField(required=True)
	confirm_new_password 		= serializers.CharField(required=True)


