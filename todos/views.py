from django.shortcuts import render, redirect
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        new_todo = Todo(title=request.POST['title'], description=request.POST['description'])
        new_todo.save()
        return redirect('list')
    return render(request, 'todos/add_todo.html')

def update_todo(request, id):
    todo = Todo.objects.get(id=id)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.save()
        return redirect('list')
    return render(request, 'todos/update_todo.html', {'todo': todo})

def delete_todo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('list')