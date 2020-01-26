from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.channel_detail)

urlpatterns = [
    path('', include(router.urls)),
] 