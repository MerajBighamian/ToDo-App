from django.shortcuts import render, redirect
from .models import Task
from .forms import *


# Create your views here.

# view of render index page of todo app (main page)
def index(request):
    tasks = Task.objects.all() # get all tasks records from Task model
    form = TaskForm() # define form instance from TaskForm (this is model form)

    if request.method == 'POST': # check request method should be POST method
        form = TaskForm(request.POST) # binding request data of form sending with POST method to TaskForm model form
        if form.is_valid(): # validate fields of form
            form.tilte = request.POST['title']
            form.save() # save fields of form in model
        return redirect('/') # redirect user to index page

    # context of index page
    context = {
        'form': form,
        'tasks': tasks,
    }
    return render(request, 'task/list.html', context) # render and return index page (with template)

"""
define this view for update tasks in model
"""
def updateTask(request, pk): # get request object and url variable (pk number)
    task = Task.objects.get(id=pk) # get object from Task model with id by value pk variable
    form = TaskForm(instance=task) # define form and binding data of model to this model form

    if request.method == 'POST': # check request method should be POST method
        form = TaskForm(request.POST, instance=task) # define form and binding model and request form to TaskForm model form

        if form.is_valid(): # validate fields of form
            form.title = request.POST['title']
            form.save() # save updated data to database
            return redirect('/') # redirect user to index page
        
    # context of update task page
    context = {
        'form': form,
    }

    return render(request, 'task/update_task.html', context) # render and return index page (with template)


"""
define this view for delete tasks in model
"""
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST': # check request method should be POST method
        task.delete() # delete task from model
        return redirect('/') # redirect user to index page

    # context of delete task page
    context = {
        'task': task,
    }

    return render(request, 'task/delete.html', context) # render and return index page (with template)
