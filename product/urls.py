from django.urls import path
from .views import Product_List,Product_Details

urlpatterns = [
    path('',Product_List.as_view(),name='product-list'),
    path('<int:pk>',Product_Details.as_view(),name='product-details')
]