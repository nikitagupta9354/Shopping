from django.urls import path
from .views import Order_List,Order_Details


urlpatterns = [
    path('',Order_List.as_view(),name='order-list'),
    path('<int:pk>',Order_Details.as_view(),name='order-details'),
    
]