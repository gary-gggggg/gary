from django.urls import path

from . import views

urlpatterns = [
    # http://127.0.0.1:31415/v1/topics/<author_id>
    path('<str:author_id>', views.TopicView.as_view()),
]
