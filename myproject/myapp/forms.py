from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from django import forms
from django.contrib.auth.models import User
class Register(UserCreationForm):
    email =forms.EmailField()
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
class Signin(AuthenticationForm):
    pass

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'phone', 'image' ]




