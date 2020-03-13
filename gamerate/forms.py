from django import forms
from gamerate.models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = {'username', 'password',}

class UserProfileForm(forms.modelForm):

    class Meta:
        model = UserProfile
        fields = {'profile_images'}