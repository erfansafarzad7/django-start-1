from django import forms

class CreateTodoForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    c_time = forms.DateTimeField()