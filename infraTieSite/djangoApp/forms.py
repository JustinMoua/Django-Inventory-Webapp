from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#These forms can be used within Django views to handle user registration and authentication processes. They provide a convenient way to generate HTML forms with appropriate fields and validation.
class LoginForm(forms.Form): #https://freedium.cfd/https://medium.com/@devsumitg/django-auth-user-signup-and-login-7b424dae7fab
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)