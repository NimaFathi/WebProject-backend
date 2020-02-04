from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('posts/', views.search_posts),
    path('accounts/', views.search_users),
    path('channels/', views.search_channels),
    path('searchall/', views.search_all)
]