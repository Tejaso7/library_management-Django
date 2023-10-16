from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class books(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    edition = models.IntegerField()
    publisher = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
