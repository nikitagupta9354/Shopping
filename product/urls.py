from django.urls import path
from .views import product_details,product_list

urlpatterns = [
    path('',product_list,name='product-list'),
    path('<int:pk>',product_details,name='product-details')
]