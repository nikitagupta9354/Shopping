from django.urls import path
from .views import pay,verifyPayment

urlpatterns = [
    path('',pay, name='create-order'),
    path('verify/',verifyPayment),
]
