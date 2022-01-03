from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.clothing_create, name='clothing-create'),
    path('show/comments/reported/', views.show_reported_comments, name='comments-reported-show'),
]