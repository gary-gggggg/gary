from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:31415/v1/user/用户名
    path('<str:username>', views.UserView.as_view()),
    path("<str:username>/avatar",views.user_avatar),
]
