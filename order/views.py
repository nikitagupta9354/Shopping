from django.shortcuts import render
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .utils import get_total_amount
from .permissions import IsObjectOwner

# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def order_list(request):
    if request.method =='GET':
        orders=Order.objects.filter(user=request.user)
        serializer=OrderSerializer(orders,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=='POST':
        total_amount=get_total_amount(request)
        if total_amount!=0:
            data={'total_amount':total_amount}
            serializer=OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Error':'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def order_details(request,pk):
    order = Order.objects.get(pk=pk)

    if not IsObjectOwner().has_object_permission(request, None, order):
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    if request.method=='GET':
        serializer=OrderSerializer(order)
        return Response(serializer.data,status=status.HTTP_200_OK)
        
        
    