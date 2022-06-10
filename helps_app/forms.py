from django import forms
from .models import HelpRequest

class CteateRequest(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['title', 'city', 'text', 'contacts', 'date_default']
        labels = {
            'title': 'Тип помощи',
            'city': 'Город',
            'text': 'Детальная информация',
            'contacts': 'Контактная информация',
            'date_default': 'Дата создания',
        }
