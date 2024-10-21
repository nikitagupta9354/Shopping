from django.shortcuts import render
from rest_framework.response import Response
from .models import CartItem
from .serializers import CartItemSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsObjectOwner


# Create your views here.


class Cart_List(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        carts=CartItem.objects.filter(user=request.user)
        serializer=CartItemSerializer(carts,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
class Cart_Update(APIView):
    permission_classes=[IsAuthenticated]
    def patch(self,request,pk):
        cart = get_object_or_404(CartItem,pk=pk)
        if not IsObjectOwner().has_object_permission(request, None, cart):
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer=CartItemSerializer(cart,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        cart = get_object_or_404(CartItem,pk=pk)
        if not IsObjectOwner().has_object_permission(request, None, cart):
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
        
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
        
        
        
        
    
    

        