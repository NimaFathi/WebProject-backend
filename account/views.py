from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import RegistrationSerializer, AccountPropertiesSerializer, ChangePasswordSerializer, SocialSerializer
from account.models import Account
from rest_framework_simplejwt.tokens import RefreshToken , AccessToken


from django.http import JsonResponse
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from requests.exceptions import HTTPError
 
from social_django.utils import load_strategy, load_backend
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden

from django.contrib.auth import logout

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        logout(request)
        data = {'Response':'successful'}
        return Response(data)




class SocialLoginView(generics.GenericAPIView):
    """Log in using google"""
    serializer_class = SocialSerializer
    permission_classes = [permissions.AllowAny]
 
    def post(self, request):
        """Authenticate user through the provider and access_token"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = serializer.data.get('provider', None)
        strategy = load_strategy(request)
 
        try:
            backend = load_backend(strategy=strategy, name=provider,
            redirect_uri='localhost:8000/mainpage')
 
        except MissingBackend:
            return Response({'error': 'Please provide a valid provider'},
            status=status.HTTP_400_BAD_REQUEST)
        try:
            if isinstance(backend, BaseOAuth2):
                access_token = serializer.data.get('access_token')
            user = backend.do_auth(access_token)
        except HTTPError as error:
            return Response({
                "error": {
                    "access_token": "Invalid token",
                    "details": str(error)
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        except AuthTokenError as error:
            return Response({
                "error": "Invalid credentials",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)
 
        try:
            authenticated_user = backend.do_auth(access_token, user=user)
       
        except HTTPError as error:
            return Response({
                "error":"invalid token",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)
       
        except AuthForbidden as error:
            return Response({
                "error":"invalid token",
                "details": str(error)
            }, status=status.HTTP_400_BAD_REQUEST)
 
        if authenticated_user and authenticated_user.is_active:
            #generate JWT token
            login(request, authenticated_user)
            data={
                "token": jwt_encode_handler(
                    jwt_payload_handler(user)
                )}
            #customize the response to your needs
            response = {
                "email": authenticated_user.email,
                "username": authenticated_user.username,
                "token": data.get('token')
            }
            return Response(status=status.HTTP_200_OK, data=response)




# Register
# Response: https://gist.github.com/mitchtabian/c13c41fa0f51b304d7638b7bac7cb694
# Url: https://<your-domain>/api/account/register
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_view(request):

    if request.method == 'POST':
        data = {}
        email = request.data.get('email', '0').lower()
        if validate_email(email) != None:
            data['error_message'] = 'That email is already in use.'
            data['response'] = 'Error'
            return Response(data)

        username = request.data.get('username', '0')
        if validate_username(username) != None:
            data['error_message'] = 'That username is already in use.'
            data['response'] = 'Error'
            return Response(data)
        password = request.data.get('password', '0')
        val = validate_password(password) 
        if val[0] == None:
            data['error_message'] = val[1]
            data['response'] = 'Error'
            return Response(data)

        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()
            account.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            data['pk'] = account.pk
            x = get_tokens_for_user(account)
            data['refresh'] = x.get('refresh')
            data['access'] = x.get('access')
            return Response(data)
        else:
            data = serializer.errors
        return Response(data)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def validate_email(email):
    account = None
    try:
        account = Account.objects.get(email=email)
    except Account.DoesNotExist:
        return None
    if account != None:
        return email

def validate_username(username):
    account = None
    try:
        account = Account.objects.get(username=username)
    except Account.DoesNotExist:
        return None
    if account != None:
        return username


def validate_password(passwd): 
      
    SpecialSym =['$', '@', '#', '%'] 
    val = {0:"not None", 1:"not any error"}
      
    if len(passwd) < 6: 
        val[0] = None
        val[1] = 'password is too short!'
        return val
    if len(passwd) > 20: 
        val[0] = None
        val[1] = 'Password is too long!!'
        return val
    if not any(char.isdigit() for char in passwd): 
        val[0] = None
        val[1] = 'your password must contain at least one digit.'
        return val
    if not any(char.isupper() for char in passwd): 
        val[0] = None
        val[1] = 'your password must contain at least one uppercase alphabet.'
        return val
    if not any(char.islower() for char in passwd): 
        val[0] = None
        val[1] = 'your password must contain at least one lowercase alphabet.'
        return val
          
    if any(char in SpecialSym for char in passwd): 
        val[0] = None 
        val[1] = 'your passwrod shouldn\'t contain any of {@,#,%,$ } set'
        return val 
    return val


# Account properties
# Response: https://gist.github.com/mitchtabian/4adaaaabc767df73c5001a44b4828ca5
# Url: https://<your-domain>/api/account/
# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def account_properties_view(request):

    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountPropertiesSerializer(account)
        return Response(serializer.data)


# Account update properties
# Response: https://gist.github.com/mitchtabian/72bb4c4811199b1d303eb2d71ec932b2
# Url: https://<your-domain>/api/account/properties/update
# Headers: Authorization: Token <token>
@api_view(['PUT',])
@permission_classes((IsAuthenticated, ))
def update_account_view(request):

    try:
        account = request.user
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AccountPropertiesSerializer(account, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = 'Account update success'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# LOGIN
# Response: https://gist.github.com/mitchtabian/8e1bde81b3be342853ddfcc45ec0df8a
# URL: http://127.0.0.1:8000/api/account/login
class ObtainAuthTokenView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        context = {}

        email = request.POST.get('username')
        password = request.POST.get('password')
        account = authenticate(email=email, password=password)
        if account:
            context['response'] = 'Successfully authenticated.'
            context['pk'] = account.pk
            context['email'] = email.lower()
            x = get_tokens_for_user(account)
            context['refresh'] = x['refresh']
            context['access'] = x['access']
        else:
            context['response'] = 'Error'
            context['error_message'] = 'Invalid credentials'

        return Response(context)




@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def does_account_exist_view(request):

    if request.method == 'GET':
        email = request.GET['email'].lower()
        data = {}
        try:
            account = Account.objects.get(email=email)
            data['response'] = email
        except Account.DoesNotExist:
            data['response'] = "Account does not exist"
        return Response(data)



class ChangePasswordView(UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = Account
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

        # confirm the new passwords match
            new_password = serializer.data.get("new_password")
            confirm_new_password = serializer.data.get("confirm_new_password")
            if new_password != confirm_new_password:
                return Response({"new_password": ["New passwords must match"]}, status=status.HTTP_400_BAD_REQUEST)

    # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({"response":"successfully changed password"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
