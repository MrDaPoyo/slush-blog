from django import forms

class postForm(forms.Form):
    title = forms.CharField(required=True)
    content = forms.CharField(required=True)