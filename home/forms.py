from django import forms
from .models import Todo

class CreateTodoForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    c_time = forms.DateTimeField()

class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'body')