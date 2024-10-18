from django.urls import path
from .views import CreatePaymentIntent

urlpatterns = [
    path('', CreatePaymentIntent.as_view(), name='create-order'),
]
