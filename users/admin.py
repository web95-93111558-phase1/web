from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

UserAdmin.list_display = list(UserAdmin.list_display) + ['defaultBlog']


		
admin.site.register(MyUser,UserAdmin)
