from django.urls import path, include
from . import views
from rest_framework import routers



app_name = 'account'

urlpatterns = [
    path('register/' , views.registration_view)

]