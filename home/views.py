from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Todo

# def say_hello(request):
#     return HttpResponse('Hello World!')

# def home_page(request):
#     return render(request, 'home.html', {'name':'Jack'})


def get_todos(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos':todos})


def details(request, todo_id):
    todo_details = Todo.objects.get(id=todo_id)
    return render(request, 'details.html', {'todo':todo_details})

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('home')

