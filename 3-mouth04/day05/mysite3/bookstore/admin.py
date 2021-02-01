from django.contrib import admin
from bookstore.models import Book


# Register your models here.
class BookManage(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub', 'price', 'market_price']
    list_display_links = ['title']
    list_filter = ['pub']
    search_fields = ['title', 'pub', 'price']
    # list_editable = ['title']


# 注册
admin.site.register(Book, BookManage)
