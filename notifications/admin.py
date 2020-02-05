from django.contrib import admin
from .models import follow_notification

# Register your models here.

@admin.register(follow_notification)
class Follow_notificationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'following' , 'follower')
    search_fields = ('pk', 'following')
    readonly_fields = ('pk',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()