from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.all_clothing_list, name='clothing-list'),
    # path('show/filter/<pk>/', views.clothing_list_filtered, name='clothing-list-filtered'),
    path('show/<int:pk>/', views.clothing_detail, name='clothing-detail'),
    path('show/<int:pk>/vote/<str:up_or_down>/', views.vote, name='clothing-vote'),
    path('add/', views.clothing_create, name='clothing-create'),
    path('delete/<int:pk>/', views.clothing_delete, name='clothing-delete'),
]