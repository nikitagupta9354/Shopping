from rest_framework import serializers

from product.models import Category, Product

# Define the Product model serializer
class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)


class ProductSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=100)
    description=serializers.CharField(max_length=200)
    price=serializers.DecimalField(max_digits=10,decimal_places=2)
    category_id= serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    inventory=serializers.IntegerField()
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name= validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.category_id= validated_data.get('category_id', instance.category_id) 
        instance.inventory = validated_data.get('inventory', instance.inventory)
        instance.save()
        return instance
        