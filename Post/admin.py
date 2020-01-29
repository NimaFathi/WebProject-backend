from django.contrib import admin
from .models import Card, Comment



# Register your models here.


class CommentAdminInline(admin.StackedInline):
    model = Comment
    extra = 1

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title', 'author', 'channel')
    search_fields = ('id','email', 'username')
    readonly_fields = ('id', )
    inlines = (CommentAdminInline, )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'time')
    search_fields = ('pk' , )
    readonly_fields = ('pk', )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
