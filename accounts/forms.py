from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password1', 'password2')


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class UpdatePasswordForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['password',]

    def clean(self):
        cleaned_data = super(UpdatePasswordForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']