from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'account'

urlpatterns = [
    path('register/' , views.registration_view, name="register"),
    path('login', obtain_auth_token ,name='login'),

]