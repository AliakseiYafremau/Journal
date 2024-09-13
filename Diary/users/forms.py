from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Enter name', max_length=100)
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput, max_length=100)
