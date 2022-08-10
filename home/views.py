from django.shortcuts import render
# from django.http import HttpResponse
from .models import Todo

# def say_hello(request):
#     return HttpResponse('Hello World!')

# def home_page(request):
#     return render(request, 'home.html', {'name':'Jack'})


def get_todos(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos':todos})


