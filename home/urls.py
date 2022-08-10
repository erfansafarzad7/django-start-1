from django.urls import path
from . import views

urlpatterns = [
    # path('hello/', views.say_hello),
    # path('home/', views.home_page),
    path('', views.get_todos),
    path('details/<int:todo_id>/', views.details, name='details')
]