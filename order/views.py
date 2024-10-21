from django.shortcuts import render
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .utils import get_total_amount
from .permissions import IsObjectOwner

# Create your views here.


class Order_List(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        orders=Order.objects.filter(user=request.user)
        serializer=OrderSerializer(orders,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        total_amount=get_total_amount(request)
        if total_amount!=0:
            data={'total_amount':total_amount}
            serializer=OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Error':'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

class Order_Details(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        order = get_object_or_404(Order,pk=pk)

        if not IsObjectOwner().has_object_permission(request, None, order):
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
       
        serializer=OrderSerializer(order)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
    