from django.contrib import admin
from .models import Channel
from Post.models import Card


class cardInline(admin.StackedInline):
    model = Card
    extra = 0


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('pk' ,'admin', 'name')
    search_fields = ('pk','email', 'username')
    inlines = (cardInline, )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
