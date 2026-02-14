# tasks/forms.py
from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'category']
        widgets = {
            'category': forms.Select(choices=Category.objects.all().values_list('id', 'name')),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']