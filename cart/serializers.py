from rest_framework import serializers
from .models import CartItem
from product.models import Product
from user.models import User


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields = ('product', 'quantity')
    

    