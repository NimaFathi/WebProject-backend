from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cards', views.CardView)
router.register(r'comments', views.CommentView)
router.register(r'hottest', views.hottest)
router.register('newest', views.newest)

urlpatterns = [
    path('', include(router.urls)),
]