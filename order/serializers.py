from rest_framework import serializers
from user.models import User
from .models import Order
from cart.models import CartItem

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['total_amount','status', 'created_at']
    

   