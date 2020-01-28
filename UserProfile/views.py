from rest_framework import viewsets
from account.models import Account
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import Account
from rest_framework import generics
from account.serializers import RegistrationSerializer

class profile_view(APIView):
    def post(self, request):
        if(request.data['method'] == 'get_user'):
            user_id = int(request.data['user_id'])
            account1 = Account.objects.filter(id = user_id)
            serializer = RegistrationSerializer(account1, many = True)
            return Response(serializer.data)
        
        elif(request.data['method'] == 'update'):
            user_id = int(request.data['user_id'])
            account1 = Account.objects.filter(id = user_id)
            account1.update(email = request.data['email'])
            serializer = RegistrationSerializer(account1, many = True)
            return Response(serializer.data)
