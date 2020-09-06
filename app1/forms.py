from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    Confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        Confirm_password = self.cleaned_data.get('Confirm_password')

        if password and Confirm_password and password != Confirm_password:
            raise ValidationError("Password don't match")

        return Confirm_password

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'Confirm_password', 'username']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Age', 'Image']
