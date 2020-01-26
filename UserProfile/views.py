from .serializers import UserSerializer
from rest_framework import viewsets
from .models import UserProfile


class UserProf(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
