from django.urls import path
from .views import cart_list,cart_update

urlpatterns = [
    path('',cart_list,name='cart-list'),
    path('<int:pk>',cart_update,name='cart-update'),
]