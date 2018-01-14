from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class NewPostForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(),
        max_length=255,
        help_text='The max length of the text is 255.'
    )

    class Meta:
        model = Post
        fields = ['rate', 'name', 'location', 'message']


class PostScheduleForm(forms.ModelForm):
    hour_count = forms.IntegerField()

    class Meta:
        model = Post
        fields = ['location']


