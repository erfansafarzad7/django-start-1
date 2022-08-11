from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()