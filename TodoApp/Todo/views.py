from django.views.generic import (
    ListView, FormView, UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.contrib import messages

from . models import Todo
from . forms import TodoForm, TodoUpdateForm

class CrearTodoFormView(FormView):
    form_class = TodoForm
    success_url = reverse_lazy('todo_app:todo-list')
    def form_valid(self, form):
        user = self.request.user
        Todo.objects.create(
            name = form.cleaned_data['name'],
            description = form.cleaned_data['description'],
            user = user
        )
        return super(CrearTodoFormView, self).form_valid(form)


class TodoListView(CrearTodoFormView ,LoginRequiredMixin ,ListView):
    model = Todo
    template_name = "todo_list.html"
    context_object_name = 'todo'
    login_url = reverse_lazy('accounts_app:sign-up')

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.listarTareasActuales(user)


class TodoUpdateView(UpdateView):
    model = Todo
    template_name = "update_todo.html"
    form_class = TodoUpdateForm
    success_url = reverse_lazy('todo_app:todo-list')

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.save()
        messages.success(self.request, f'La tarea {todo.name} ah sido actualizada correctamente')
        return super(TodoUpdateView, self).form_valid(form)

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "delete_todo.html"
    success_url = reverse_lazy('todo_app:todo-list')




