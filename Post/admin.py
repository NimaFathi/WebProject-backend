from django.contrib import admin
from .models import Card, Comment



# Register your models here.

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
