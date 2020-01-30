from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('hottest/', views.hottest),
    path('newest/', views.newest),
    path('following/', views.following),
    path('contributes/', views.contributes)
]