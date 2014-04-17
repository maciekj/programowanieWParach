from django.contrib import admin
from models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    can_delete = False
    verbose_name_plural = 'userprofile'

admin.site.register(UserProfile, UserProfileAdmin)