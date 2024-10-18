# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

class CreatePaymentIntent(APIView):
    def post(self, request):
        try:
            amount = request.data.get('amount')  # Amount
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='inr',
                payment_method_types=['card'],
            )
            return Response({'clientSecret': payment_intent['client_secret']}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
