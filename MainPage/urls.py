from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'hottest', views.hottest)
router.register(r'newest', views.newest)

urlpatterns = [
    path('', include(router.urls)),
]