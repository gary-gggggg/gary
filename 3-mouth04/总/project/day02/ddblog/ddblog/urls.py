"""ddblog URL Configuration

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
from django.urls import path

from ddblog import views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_cross', views.test_cross),
    path('test_cross_server', views.test_cross_server),
    # 下一个是基于CBV,CBV：模型模块名，视图类，as_view()
    # as_view()的作用根据请求方法，在视图类中查找对应的类，找到后调用，找不到的话就报错（405）
    # 但是因为as_view是后台处理的，所以那边类里面的函数名需要和请求的方式一模一样。
    path('v1/users', user_views.UserView.as_view()),

]
