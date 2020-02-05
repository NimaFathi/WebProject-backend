from django.contrib import admin
from .models import Card, Comment, Image
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class CommentAdminInline(admin.StackedInline):
    model = Comment
    extra = 1
class InlineImage(admin.TabularInline):
    model = Image

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('pk' ,'title', 'author', 'channel')
    search_fields = ('pk','title',)
    readonly_fields = ('pk', )
    inlines = (CommentAdminInline,InlineImage )
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
