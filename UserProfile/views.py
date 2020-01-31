from rest_framework import viewsets
from account.models import Account
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import Account
from rest_framework import generics
from account.serializers import RegistrationSerializer
from account.serializers import ProfileSerializer


class change_profile(APIView):
    def post(self, request):
        user_id = int(request.data['user_id'])
        account1 = Account.objects.filter(id = user_id)
        account1.update(occupy = request.data['occupy'])
        account1.update(bio = request.data['bio'])
        serializer = ProfileSerializer(account1, many = True)
        return Response(serializer.data)


class user_profile(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = Account.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        queryset = queryset.filter(id = user_id)
        return queryset
