from django.shortcuts import render, redirect
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator


def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
           form.save()
        messages.success(request, 'New Task Added!')
        return redirect('todolist')
        
    else:
        tasks = TaskList.objects.all()
        paginator = Paginator(tasks, 5)
        page = request.GET.get('pg')
        tasks = paginator.get_page(page)
        return render(request, 'todolist/todolist.html', {'tasks':tasks})

def contact(request):
    context = {}
    context['contact_text'] = 'Welcome to Contact Page.'
    return render(request, 'todolist/contact.html', context)

def about(request):
    context = {}
    context['about_text'] = 'Welcome to About Page.'
    return render(request, 'todolist/about.html', context)

def index(request):
    context = {}
    context['index_text'] = 'Welcome to Index Page.'
    return render(request, 'todolist/index.html', context)


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == 'POST':
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, 'Task Edited!')
        return redirect('todolist')
    else:
        task = TaskList.objects.get(pk=task_id)
        return render(request, 'todolist/edit.html', {'task':task})

    
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = True
    task.save()
    return redirect('todolist')

def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    return redirect('todolist')