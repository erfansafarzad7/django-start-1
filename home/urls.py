from django.urls import path
from . import views

urlpatterns = [
    # path('hello/', views.say_hello),
    # path('home/', views.home_page),
    path('', views.get_todos, name='home'),
    path('details/<int:todo_id>/', views.details, name='details'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete'),
]