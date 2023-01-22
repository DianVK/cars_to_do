from django.urls import path
from base.views import TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),

]