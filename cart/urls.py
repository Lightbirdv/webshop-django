from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:pk>/', views.add_shopping_cart, name='shopping-cart-add'),
    path('show/', views.show_shopping_cart, name='shopping-cart-show'),
    path('pay/', views.pay, name='shopping-cart-pay'),
]