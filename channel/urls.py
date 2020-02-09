from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('create/', views.create_channel),
    path('editchannel/', views.edit_channel),
    path('info/', views.channel_view),
    path('userchannels/', views.user_channels),
    path('removeauthor/', views.remove_author),
    path('addfollower/', views.add_follower),
    path('removefollower/', views.remove_follower),
    path('channelfollowers/', views.get_followers)
]
