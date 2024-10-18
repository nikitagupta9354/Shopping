from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import razorpay
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


client = razorpay.Client(auth=("rzp_test_M0WqjmvfMzlcHw", "RZK3OjLDtOqiK7zQf1T61m2e"))

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@csrf_exempt  
def pay(request):
    if request.method == 'POST': 
        amount = 50000 
        currency = 'INR'
        order = client.order.create({'amount': amount, 'currency': currency ,'payment_capture': 1 })
        return Response(order)
    
    
@api_view(['POST'])

def verifyPayment(request):
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
