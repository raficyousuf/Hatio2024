from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, TodoItem
from .forms import TodoItemForm, ProjectForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    todos = project.todos.all()
    return render(request, 'project_detail.html', {'project': project, 'todos': todos})

def add_todo(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.project = project
            todo.save()
            return redirect('project_detail', pk=project_pk)
    else:
        form = TodoItemForm()
    return render(request, 'todo_form.html', {'form': form})

# todo/views.py


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'todo_form.html', {'form': form})


def edit_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=todo.project.pk)
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todo_form.html', {'form': form})

def mark_complete(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.completed = True
    todo.save()
    return redirect('project_detail', pk=todo.project.pk)
