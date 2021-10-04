from django import forms
from django.forms import fields
from .models import Depto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Depto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields =  ['username', "first_name", "last_name", "email", "password1", "password2"]