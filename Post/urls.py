from django.urls import path, include
from . import views
from rest_framework import routers
from .views import detail_card_view, detail_comment_view, delete_comment_view, delete_card_view, update_card_view, \
    update_comment_view, create_card_view, create_comment_view, is_author_of_card, is_author_of_comment

urlpatterns = [
    path('card/<int:id>', detail_card_view, name="detail_card"),
    path('card/update/<int:id>/', update_card_view, name="update_card"),
    path('card/delete/<int:id>', delete_card_view, name="delete_card"),
    path('card/create/', create_card_view, name="create_card"),
    path('card/is_author/<int:id>', is_author_of_card, name="is_author_card"),

    path('comment/<int:id>', detail_comment_view, name="detail_comment"),
    path('comment/update/<int:id>/', update_comment_view, name="update_comment"),
    path('comment/delete/<int:id>', detail_comment_view, name="delete_comment"),
    path('comment/create/', create_comment_view, name="create_comment"),
    path('comment/is_author/<int:id>', is_author_of_comment, name="is_author_comment"),

]