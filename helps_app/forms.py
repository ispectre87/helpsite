from django import forms
from .models import HelpRequest

class CteateRequest(forms.ModelForm):
    class Meta:
        model = HelpRequest
