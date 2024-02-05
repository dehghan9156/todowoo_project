from django.shortcuts import render,redirect,get_object_or_404
from .forms import TodoCreateForm
from django.contrib import messages
from .models import Todo
def createtodo(request):
    if request.method == 'POST' :
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.title = form.cleaned_data['title']
            new_todo.memo = form.cleaned_data['memo']
            new_todo.important = form.cleaned_data['important']
            new_todo.save()
            messages.success(request, 'todo created succssfully', 'success')
            return redirect('accounts:home')
    else:
        form = TodoCreateForm()
    return render(request, 'todo/createtodo.html', {'form': form})

def currenttodo(request):

    todos = Todo.objects.filter(user=request.user)
    return render(request,'todo/currenttodo.html',{'todos':todos})

def viewtodo(request,todo_id):
    todo = get_object_or_404(Todo,id=todo_id,user=request.user)
    if request.method == 'POST':
        form = TodoCreateForm(request.POST,instance = todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated succssfully', 'success')
            return redirect('todo:currenttodo')
    else:
        form = TodoCreateForm(instance = todo)
    return render(request,'todo/viewtodo.html',{'todo':todo , 'form':form})

def deletetodo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request,'User deleted succssfully','success')
    return redirect('todo:currenttodo')