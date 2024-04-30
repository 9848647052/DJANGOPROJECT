from django import forms
from .models import Farm
from django.contrib.auth.models import User

class FarmForm(forms.ModelForm):
    class Meta:
        model=Farm
        fields=['name','type','mdate','price']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']