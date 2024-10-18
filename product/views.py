from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Category,Product
from .serializers import CategorySerializer,ProductSerializer

# Create your views here.
@api_view(['GET','POST'])
@permission_classes([IsAdminOrReadOnly])
def product_list(request):
    if request.method=='GET':
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','PATCH','DELETE'])
@permission_classes([IsAdminOrReadOnly])
def product_details(request,pk):
    if request.method == 'GET':
        product=Product.objects.get(pk=pk)
        serializer=ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        product=Product.objects.get(pk=pk)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='PATCH':
        cart=Product.objects.get(pk=pk)
        serializer=ProductSerializer(cart,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    if request.method=='DELETE':
        product=Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
