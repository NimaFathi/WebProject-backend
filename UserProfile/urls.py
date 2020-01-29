from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('change_profile/', views.change_profile.as_view()),
    path('profile/', views.user_profile.as_view())
]