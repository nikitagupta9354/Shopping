from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import razorpay
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from order.models import Order


client = razorpay.Client(auth=("rzp_test_M0WqjmvfMzlcHw", "RZK3OjLDtOqiK7zQf1T61m2e"))


class Pay(APIView): 
    permission_classes=[IsAuthenticated]
    
    def post(self,request):
            order=Order.objects.get(user=request.user,status='Pending')
            amount =int(order.total_amount*100)
            currency = 'INR'
            order = client.order.create({'amount': amount, 'currency': currency ,'payment_capture': 1 })
            return Response(order)
    
    

class VerifyPayment(APIView):
    def post(self,request):
            try:
                
                payment_id = request.data.get('razorpay_payment_id')
                order_id = request.data.get('razorpay_order_id')
                signature = request.data.get('razorpay_signature')

            
                params_dict = {
                    'razorpay_order_id': order_id,
                    'razorpay_payment_id': payment_id,
                    'razorpay_signature': signature
                }

                
                client.utility.verify_payment_signature(params_dict)

                return Response({'status': 'Payment verified successfully'}, status=status.HTTP_200_OK)

            except razorpay.errors.SignatureVerificationError:
                return Response({'error': 'Signature verification failed'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
