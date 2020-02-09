from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('follows/', views.follow_notifications),
    path('comments/', views.comment_notifications),
    path('notificationscount/', views.notifications_count)
]