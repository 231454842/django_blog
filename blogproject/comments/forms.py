from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """docstring for [object Object]."""
    class Meta:
        model=Comment
        fields = ['name', 'email', 'url', 'text']
