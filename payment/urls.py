from django.urls import path
from .views import Pay,VerifyPayment

urlpatterns = [
    path('',Pay.as_view(), name='create-order'),
    path('verify/',VerifyPayment.as_view()),
]
