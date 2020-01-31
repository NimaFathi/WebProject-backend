
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url 


urlpatterns = [
    path('raeis/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('UserProfile/', include('UserProfile.urls')),
    path('post/', include('Post.urls')),
    path('channel/', include('channel.urls')),
    path('account/', include('account.urls')),
    path('mainpage/',include('MainPage.urls')),
    path('notifications/', include('notifications.urls')),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
