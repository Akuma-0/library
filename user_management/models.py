from django.db import models
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
# Create your models here.

class ProfileEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
