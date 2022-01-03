from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.all_clothing_list, name='clothing-list'),
    path('show/<int:pk>/', views.clothing_detail, name='clothing-detail'),
    path('show/<int:pk>/vote/<str:up_or_down>/', views.vote, name='clothing-vote'),
    path('delete/<int:pk>/', views.clothing_delete, name='clothing-delete'),
    path('search/', views.clothing_search, name='clothing-search'),
]