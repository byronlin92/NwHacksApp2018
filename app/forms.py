from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post

# class SignUpForm(UserCreationForm):
#     email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

class NewPostForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(),
        max_length=255,
        help_text='The max length of the text is 255.'
    )

    class Meta:
        model = Post
        fields = ['price', 'name', 'location', 'message']