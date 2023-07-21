from django import forms
from django.forms import ModelForm
from .models import text

class textForm(ModelForm):
    class Meta:
        model = text
        fields = 'content',
        labels = {
            'content': '',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }