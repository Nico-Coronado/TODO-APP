from django.views.generic import FormView, View
from django.urls.base import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
# login
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# 
from . forms import SignUpForm, LoginForm

class SignUpFormView(FormView):
    template_name = 'sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts_app:login')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password1 = form.cleaned_data['password1']

        user = User.objects.create(
            username = username
        )
        user.set_password(password1)
        user.save()
        messages.success(self.request, f'Se ah creado con exito al usuario {username}')
        return super(SignUpFormView, self).form_valid(form)

class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('todo_app:todo-list')

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)
        messages.success(self.request, f'Bienvenido {user.username}')
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'accounts_app:login'
            )
        )