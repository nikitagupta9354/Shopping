from django.db import models
from user.models import User 

class Order(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    total_amount = models.DecimalField(max_digits=10, decimal_places=2)


    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username} - Status: {self.status}"
