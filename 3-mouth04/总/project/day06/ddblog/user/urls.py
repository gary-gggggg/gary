from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:31415/v1/users/sms
    # 该行写到最上面，因为下面有path转换器
    path('sms',views.sms_views),
    # http://127.0.0.1:31415/v1/user/用户名
    path('<str:username>', views.UserView.as_view()),
    # http://127.0.0.1:31415/v1/user/用户名/avatar
    path("<str:username>/avatar",views.user_avatar),

]
