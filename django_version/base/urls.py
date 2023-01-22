from django.urls import path
from . import views

urlspatterns = [
    path('', views.taskList, name='tasks'),

]