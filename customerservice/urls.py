from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.clothing_create, name='clothing-create'),
    path('edit/<int:pk>/', views.clothing_update, name='clothing-update'),
    path('show/comments/reported/', views.show_reported_comments, name='comments-reported-show'),
    path('delete/comments/reported/<int:pk>/', views.delete_reported_comments, name='comments-reported-delete')
]