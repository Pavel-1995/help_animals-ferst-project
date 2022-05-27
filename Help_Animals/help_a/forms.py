from django import forms
from .models import Animals
from django.forms import ModelForm


class AnimalsForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = ('title', 'slug', 'content', 'photo', 'cat')
        widgets = {
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'Enter your text'})}
