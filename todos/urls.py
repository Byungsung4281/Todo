# todos/urls.py
from django.urls import path
from .views import todo_list, add_todo, update_todo, delete_todo

urlpatterns = [
    path('', todo_list, name='list'),
    path('add/', add_todo, name='add'),
    path('update/<int:id>/', update_todo, name='update'),
    path('delete/<int:id>/', delete_todo, name='delete'),
]