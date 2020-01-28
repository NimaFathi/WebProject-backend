from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token

@api_view(['POST',])
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered a new user'
            data['email'] = account.email
            data['username'] = account.username
            data['id'] = account.pk
            token = Token.obejects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)