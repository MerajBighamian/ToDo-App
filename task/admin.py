from django.contrib import admin

# import all model of task app
from task.models import Task

# Register your models here.

# register task app
admin.site.register(Task)
