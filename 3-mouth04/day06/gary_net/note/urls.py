from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_view),
    path('add',views.add_view),
    # path('',views.add_view),
    # path('add',views.add_view),
]
