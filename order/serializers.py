from rest_framework import serializers
from user.models import User
from .models import Order
from cart.models import CartItem

class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    total_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    status = serializers.CharField(max_length=20,required=False)
    created_at = serializers.DateTimeField(read_only=True)
    
    def create(self,validated_data):
        return Order.objects.create(**validated_data)
    
    def validate_total_amount(self,value):
        if value==0:
            raise serializers.ValidationError("Cart is empty")

   