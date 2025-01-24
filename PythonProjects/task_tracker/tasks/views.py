from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Tasks

# Create your views here.

# Read: Display the list of tasks
class TaskListView(ListView):
    model = Tasks
    template_name = 'tasks/task_list.html' #HTML template for listing tasks
    context_object_name = 'tasks'
# create: add a new task
class TaskCreateView(CreateView):
    model = Tasks
    fields = ['title','description','is_completed','due_date','progress']
    template_name = 'tasks/task_form.html' # form for creating/updating tasks
    success_url = reverse_lazy('task-list') # Redirect after successful creation
class TaskUpdateView(UpdateView):
    model = Tasks
    fields = ['title', 'description', 'due_date', 'progress', 'is_completed']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')
# Delete: Remove a task
class TaskDeleteView(DeleteView):
    model = Tasks
    template_name = 'tasks/task_confirm_delete.html'  # Confirmation page
    success_url = reverse_lazy('task-list')