from django.urls import path

from . import views

app_name = 'accounts_app'

urlpatterns = [
    path('sign-up/', views.SignUpFormView.as_view(), name='sign-up'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]