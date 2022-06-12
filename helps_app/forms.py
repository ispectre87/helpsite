from django import forms
from .models import HelpRequest

class CreateRequest(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['title', 'text', 'contacts']
        labels = {
            'title': 'Тип помощи',
            'text': 'Детальная информация',
            'contacts': 'Контактная информация',
        }
