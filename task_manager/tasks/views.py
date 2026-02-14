from rest_framework import viewsets
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Category
from .forms import TaskForm
from datetime import datetime

def task_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        
        if task_form.is_valid():
            task_form.save() 
            return redirect('/')
        else:
            print(task_form.errors)  # Print form errors to the console for debugging
    else:
        task_form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'task_form': task_form, 'categories': categories})

def task_update(request, pk):
    categories = Category.objects.all()
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        
        if task_form.is_valid():
            task_form.save()  # Update the task with the selected category
            return redirect('/')
        else:
            print(task_form.errors)  # Print form errors to the console for debugging
    else:
        task_form = TaskForm(instance=task)
    
    return render(request, 'tasks/task_form.html', {'task_form': task_form, 'categories': categories})

def task_list(request):
    tasks = Task.objects.all()  # Start with all tasks
    categories = Category.objects.all()
    # Filter by category if provided
    category_filter = request.GET.get('category')
    if category_filter:
        tasks = tasks.filter(category__name=category_filter)

    # Filter by task name if provided
    name_filter = request.GET.get('name')
    if name_filter:
        tasks = tasks.filter(name__icontains=name_filter)

    # Filter by due date if provided
    date_filter = request.GET.get('due_date')
    if date_filter:
        try:
            # Parse the date string into a datetime object
            due_date = datetime.strptime(date_filter, '%Y-%m-%d').date()
            tasks = tasks.filter(due_date=due_date)
        except ValueError:
            pass  # Handle invalid date format gracefully

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'categories': categories})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'category__name']
    filterset_fields = ['created_at']
    
def index(request):
    return render(request, 'index.html')
