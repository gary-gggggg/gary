from django.contrib import admin
from .models import *


# Register your models here.
class AuthorManage(admin.ModelAdmin):
    list_display = ['id', 'name']


class WifeManage(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Author, AuthorManage)
admin.site.register(Wife,WifeManage)
