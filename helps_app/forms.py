from django import forms
from .models import HelpRequest
from django.contrib.auth.forms import UserCreationForm, User
from captcha.fields import CaptchaField


class CreateRequest(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['title', 'text', 'contacts']
        labels = {
            'title': 'Тип помощи',
            'text': 'Детальная информация',
            'contacts': 'Контактная информация',
        }
        widgets = {
            'title': forms.Textarea(attrs={'cols': 60, 'rows': 2}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 8}),
            'contacts': forms.Textarea(attrs={'cols': 60, 'rows': 4}),
        }

class UserRegister(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form_input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form_input'}))
    password2 = forms.CharField(label='Пароль дубль два', widget=forms.PasswordInput(attrs={'class':'form_input'}))
    captcha = CaptchaField()
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')