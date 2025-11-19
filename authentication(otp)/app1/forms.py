from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from app1.models import Customuser

class Signupform(UserCreationForm):
    role_choices = (('teacher', 'Teacher'),('student', 'Student'))
    role = forms.ChoiceField(choices=role_choices)
    class Meta:
        model=Customuser
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name','phone','role']


class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()