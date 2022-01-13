from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import MyUser
from django import forms


class MySignUpForm(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'txt__input', 'type':'password', 'placeholder':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'txt__input', 'type':'password', 'placeholder':'password'}),
    )


    class Meta:
        model = MyUser
        fields = ('username','first_name','last_name','email','profile_picture')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'txt__input', 'placeholder':'username'}),
            'first_name': forms.TextInput(attrs={'class': 'txt__input', 'placeholder':'firstname'}),
            'last_name': forms.TextInput(attrs={'class': 'txt__input', 'placeholder':'lastname'}),
            'email': forms.EmailInput(attrs={'class': 'txt__input', 'placeholder':'email'}),
        }

class MyLoginForm(AuthenticationForm):

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'txt__input', 'type':'password', 'placeholder':'password'}),
    )

    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class':'txt__input', 'placeholder':'username'}))
            
        