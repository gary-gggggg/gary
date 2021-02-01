from django.urls import path
from payment import views

urlpatterns = [
    # http://127.0.0.1:31415/payment/jump/
    path('jump/', views.JumpView.as_view()),
    # http://127.0.0.1:31415/payment/result/
    path('result/',views.ResultView.as_view())
]
