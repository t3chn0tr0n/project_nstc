from django import forms
from .models import Temp_user

class UserForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['uname', 'email', 'password']
        widgets = {
            'first_name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'email' : forms.TextInput(attrs = {'class': 'form-control'}),
        }