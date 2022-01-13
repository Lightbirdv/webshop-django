from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.all_clothing_list, name='clothing-list'),
    path('show/men/', views.clothing_list_men, name='clothing-list-men'),
    path('show/women/', views.clothing_list_women, name='clothing-list-women'),
    path('show/<int:pk>/', views.clothing_detail, name='clothing-detail'),
    path('show/women/<int:pk>/', views.clothing_detail, name='clothing-detail'),
    path('show/men/<int:pk>/', views.clothing_detail, name='clothing-detail'),
    path('show/filter/<str:filter>/', views.filtered_clothing_list, name='clothing-filter'),
    path('show/men/filter/<str:filter>/', views.filtered_clothing_list_men, name='clothing-filter-men'),
    path('show/women/filter/<str:filter>/', views.filtered_clothing_list_women, name='clothing-filter-women'),
    path('delete/clothing/<int:pk>/', views.clothing_delete, name='clothing-delete'),
    path('search/', views.clothing_search, name='clothing-search'),
    path('create/comment/<int:pk>/', views.comment_create, name='comment-create'),
    path('report/comment/<int:pk>/', views.comment_report, name='comment-report'),
]