from django.urls import path
from zhixueshequ import views

urlpatterns = [
    # 127.0.0.1：31415/zhixueshequ/index
    path('index', views.index_view)
]
