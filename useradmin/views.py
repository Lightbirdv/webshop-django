from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout
)
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
from .forms import MySignUpForm
from .models import MyUser


class MySignUpView(generic.CreateView):
    form_class = MySignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    

class MyLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())


class MyUserListView(generic.ListView):
    model = MyUser
    context_object_name = 'all_myusers'
    template_name = 'myuser-list.html'


def logout_view(request):
    auth_logout(request)
    return render(request, 'logout.html')

def profile_view(request):
    user = MyUser.objects.get(id=request.user.id)
    context = {'that_user': user}
    return render(request, 'profile.html', context)