from django.contrib import admin
from .models import *


# Register your models here.
class PublisherManage(admin.ModelAdmin):
    list_display = ['id', 'name']


class BookManage(admin.ModelAdmin):
    list_display = ['id', 'title', 'publisher']


admin.site.register(Publisher, PublisherManage)
admin.site.register(Book,BookManage)
