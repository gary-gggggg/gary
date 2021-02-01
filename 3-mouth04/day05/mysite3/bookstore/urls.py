from django.urls import path
from . import views
urlpatterns = [
    path('all_book', views.all_book),
    path('add_book',views.add_book),
    path('update_book/<int:bid>',views.update_book),
    path('delete_book',views.delete_book)
]
