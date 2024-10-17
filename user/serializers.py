from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','role', 'password','password2']
    extra_kwargs={
        'password': {'write_only': True}
    }
    
    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords must match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password=validated_data['password']
        user=User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
class UserLoginSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=100)
    password=serializers.CharField(style={'input_type':'password'})
    
    
    
    