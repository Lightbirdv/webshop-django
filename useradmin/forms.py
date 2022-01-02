from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class MySignUpForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('username','first_name','last_name','email')
      