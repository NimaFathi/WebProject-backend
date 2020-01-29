from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cards', views.CardView)
router.register(r'comments', views.CommentView)

urlpatterns = [
    path('', include(router.urls)),
]