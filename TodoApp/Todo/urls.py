from django.urls import path
from . views import (TodoListView, TodoUpdateView, TodoDeleteView)

app_name = 'todo_app'

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
    path('update/<pk>/', TodoUpdateView.as_view(), name='update'),
    path('delete/<pk>/', TodoDeleteView.as_view(), name='delete'),
]