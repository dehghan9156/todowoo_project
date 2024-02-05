from django.shortcuts import render,redirect
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
            return redirect('accounts :home')
    else:
        form = TodoCreateForm()
    return render(request, 'todo/createtodo.html', {'form': form})
