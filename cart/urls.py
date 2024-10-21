from django.urls import path
from .views import Cart_List,Cart_Update

urlpatterns = [
    path('',Cart_List.as_view(),name='cart-list'),
    path('<int:pk>',Cart_Update.as_view(),name='cart-update'),
]