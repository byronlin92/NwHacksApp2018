from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(),
        max_length=255,
        help_text='The max length of the text is 255.'
    )

    class Meta:
        model = Post
        fields = ['name', 'location', 'message']

