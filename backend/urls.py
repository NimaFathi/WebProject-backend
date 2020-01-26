
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.conf.urls import url 

urlpatterns = [
    path('raeis/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('post/', include('Post.urls'))
]
=======
from django.conf.urls import url
import UserProfile

urlpatterns = [
    path('raeis/', admin.site.urls),
    path('UserProfile/', include('UserProfile.urls')),
    url(r'^api-auth/', include('rest_framework.urls'), name='rest_framework'),
]
>>>>>>> 6c8743a27a10370dbf787df87ae1e92f517f3059
