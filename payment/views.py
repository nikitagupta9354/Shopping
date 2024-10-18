from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import razorpay

client = razorpay.Client(auth=("rzp_test_M0WqjmvfMzlcHw", "RZK3OjLDtOqiK7zQf1T61m2e"))

@api_view(['POST'])
@csrf_exempt  
def pay(request):
    if request.method == 'POST': 
        amount = 50000 
        currency = 'INR'
        order = client.order.create({'amount': amount, 'currency': currency ,'payment_capture': 1 })
        return Response(order)
    
