
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url 
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created

from rest_framework_simplejwt.views import TokenRefreshView



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
    path('search/', include('search.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('', include('social_django.urls', namespace='social')),
  	
]


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    }

    # render email text
    email_html_message = render_to_string('email/user_reset_password.html', context)
    email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()