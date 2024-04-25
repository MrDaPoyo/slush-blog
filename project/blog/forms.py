from django import forms
from .models import post

class postForm(forms.ModelForm):
    title = forms.CharField(required=True)
    content = forms.CharField(required=True)
    class Meta:
        model = post
        fields = [
            'title',
            'content'
        ]