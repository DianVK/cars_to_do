from django.shortcuts import render
from django.views.generic.list import ListView

from base.models import Task

class TaskList(ListView):
    model = Task
    