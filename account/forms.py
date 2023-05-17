from django import forms
from .models import UserBase

class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={'Required': 'Sorry, you need an email'})
    password = forms.CharField(label='Enter password', min_length=4, max_length=50, help_text='Required', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', min_length=4, max_length=50, help_text='Required', widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email',)