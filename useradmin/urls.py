from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='login'),
    path('signup/', views.MySignUpView.as_view(), name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('edit/<int:userid>/', views.user_update, name='user-update'),
]
