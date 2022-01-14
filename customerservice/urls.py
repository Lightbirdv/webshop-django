from django.urls import path
from . import views

urlpatterns = [
    path('', views.customerservice_view, name='customerservice-view'),

    path('create/clothing/', views.clothing_create, name='clothing-create'),
    path('edit/<int:pk>/', views.clothing_update, name='clothing-update'),

    path('show/comments/reported/', views.show_reported_comments, name='comments-reported-show'),
    path('delete/comments/reported/<int:pk>/', views.delete_reported_comments, name='comments-reported-delete'),

    path('show/myusers/', views.show_myusers, name='myuser-list'),
    path('delete/myusers/<int:userid>', views.delete_myusers, name='myuser-delete')
]