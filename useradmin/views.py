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
from .forms import MySignUpForm, MyLoginForm
from .models import MyUser


class MySignUpView(generic.CreateView):
    form_class = MySignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    

class MyLoginView(LoginView):
    form_class = MyLoginForm
    template_name = 'login.html'
    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())
        

def logout_view(request):
    auth_logout(request)
    return render(request, 'logout.html')

def profile_view(request):
    user = MyUser.objects.get(id=request.user.id)
    context = {'that_user': user}
    return render(request, 'profile.html', context)

def user_update(request, userid):
    if not request.user.is_requestuser_or_staff(userid):
        return redirect('profile')

    user = MyUser.objects.get(id=userid)
    form = MySignUpForm(instance=user)
    print(request.POST)
    print(request.FILES)
    if request.method == 'POST':
        if request.POST['username']:
            user.username = request.POST['username']
        if request.POST['first_name']:
            user.first_name = request.POST['first_name']
        if request.POST['last_name']:
            user.last_name = request.POST['last_name']
        if request.POST['email']:
            user.email = request.POST['email']
        if request.FILES['profile_picture']:
            user.profile_picture = request.FILES['profile_picture']
        print(user)
        user.save()

        return redirect('profile')

    context = {'form': form}
    return render(request, 'myuser-edit.html', context) 