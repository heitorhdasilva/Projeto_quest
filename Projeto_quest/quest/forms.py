from django import forms
from django.contrib.auth.models import User
from quest.models import Questionario

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class Quest(forms.ModelForm):
    data_final = forms.DateField
    titulo = forms.CharField(max_length=50)
    class Meta:
        model = Questionario
        fields = ('data_final','titulo')