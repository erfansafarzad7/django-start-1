from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import CreateTodoForm

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
    messages.success(request, 'Done!!', 'success')
    return redirect('home')

def create(request):
    if request.method == 'POST':
        form = CreateTodoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], body=cd['body'], c_time=cd['c_time'])
            messages.success(request, 'Successfully Added!..', 'success')
            return redirect('home')
    else:
        form = CreateTodoForm()
    return render(request, 'form.html', {'form':form})