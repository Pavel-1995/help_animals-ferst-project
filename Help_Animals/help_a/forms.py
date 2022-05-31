from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Animals


class AnimalsForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = ('title', 'slug', 'content', 'photo', 'cat')
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'Enter your text'})}



