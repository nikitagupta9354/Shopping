from django.shortcuts import render
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .permissions import IsObjectOwner


# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def cart_list(request):
    if request.method =='GET':
        carts=CartItem.objects.filter(user=request.user)
        serializer=CartItemSerializer(carts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=='POST':
        serializer=CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['PATCH','DELETE'])
@permission_classes([IsAuthenticated])  
def cart_update(request,pk):
    
    cart = CartItem.objects.get(pk=pk)

    if not IsObjectOwner().has_object_permission(request, None, cart):
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    if request.method=='PATCH':
        cart=CartItem.objects.get(pk=pk)
        serializer=CartItemSerializer(cart,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        cart=CartItem.objects.get(pk=pk)
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
        
        
        
        
    
    

        