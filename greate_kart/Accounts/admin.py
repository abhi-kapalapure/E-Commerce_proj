from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# signup your models here.
class AccountAdmin(UserAdmin):
    list_display =['email', 'first_name', 'username','is_active','date_joined']
    list_display_links = ['first_name','username','email']
    randomly_fields = ['last_joined',]

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# signup your models here.
admin.site.register(Account)
