"""mesite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/page/2003
    path('', views.page_index),
    #第三个参数相当于是给url配置一个名字
    #从语法的角度去理解,相当于giao这个变量的值'page/2003'
    path('page/2003',views.page_2003,name='giao'),
    path('handsomegary/2021',views.giao_314),
    #path转换器
    path('<int:num1>/<str:op>/<int:num2>',views.page_cul),
    #re_path正则查找
    re_path(r'^birthday/(?P<d>\d{1,2})/(?P<m>\d{1,2})/(?P<y>\d{4})$',views.page_bir)
    # path('page/<int:num>',views.page_number),
    # path('page/<path:data>',views.page_data)
]
