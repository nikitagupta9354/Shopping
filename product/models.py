from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200,blank=True,null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category_id=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    inventory=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
    