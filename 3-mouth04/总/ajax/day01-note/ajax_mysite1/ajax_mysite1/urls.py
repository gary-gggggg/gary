"""ajax_mysite1 URL Configuration

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

from ajax_mysite1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_xhr', views.test_xhr),
    path('test_xhr_get', views.test_xhr_get),
    path('test_xhr_get_server', views.test_xhr_get_server),
    path('test_jq_get', views.test_jq_get),
    path('test_json', views.test_json),
    path('make_json_server', views.make_json_server),
    path('register',views.register),
    path('cross',views.test_cross),
    path('cross_server',views.cross_server),


]
