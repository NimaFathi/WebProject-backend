from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import Account
from Post.models import Card

from channel.models import Channel

class ChannelAdminInline(admin.StackedInline):
    model = Channel
    extra = 0

class PostAdminInline(admin.StackedInline):
    model = Card
    extra = 1

@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('pk' ,'email', 'username', 'date_joined', 'last_login' , 'is_admin', )
    search_fields = ('pk','email', 'username')
    readonly_fields = ('pk','date_joined' , 'last_login', )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    inlines = (PostAdminInline, ChannelAdminInline )


