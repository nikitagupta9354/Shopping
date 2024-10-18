from django.urls import path
from .views import order_list,order_details


urlpatterns = [
    path('',order_list,name='order-list'),
    path('<int:pk>',order_details,name='order-details'),
    
]