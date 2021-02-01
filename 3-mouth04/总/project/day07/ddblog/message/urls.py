from django.urls import path

from message import views

urlpatterns=[
    path('<int:topic_id>',views.message_view)
]