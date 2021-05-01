from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Person
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    prime = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ['prime','username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
