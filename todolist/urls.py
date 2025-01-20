from django.urls import path
from todolist.views import task_list_create, task_list_edit

urlpatterns = [
    path('tareas/', task_list_create, name='task_list_create'),
    path('tareas/<int:pk>/', task_list_edit, name='task_list_edit'),
]