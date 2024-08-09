from django import forms
from .models import TodoItem, Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description', 'completed']