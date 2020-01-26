
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import UserProfile

urlpatterns = [
    path('raeis/', admin.site.urls),
    path('UserProfile/', include('UserProfile.urls')),
    url(r'^api-auth/', include('rest_framework.urls'), name='rest_framework'),
]