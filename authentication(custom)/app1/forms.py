from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app1.models import Customuser
class Signupform(UserCreationForm):
    class Meta:
        model=Customuser
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name','phone','address']


class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()