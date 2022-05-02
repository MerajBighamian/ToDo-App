from attr import attr
from django.forms import ModelForm
from django import forms
from matplotlib import widgets

from .models import *

"""
define model form for work with task model and edit records
"""
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task # model name of model form
        fields = ['title','complate'] # accessable fields of model
    widgets = {
        'complate' : forms.CheckboxInput(attrs={'class':'invisible'})
    }