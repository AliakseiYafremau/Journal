from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Enter name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=100)
