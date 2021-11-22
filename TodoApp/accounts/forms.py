from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label = 'Contraseña',
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingrese su contraseña'}),
    )
    password2 = forms.CharField(
        label = 'Contraseña (confirmación)',
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repita su contraseña'}),
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario'
                }
            )
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nombre de usuario',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Ingrese su nombre de usuario',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label='Contrasena',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ingrese su contrasena',
                'class': 'form-control'
            }
        )
    )
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password =  self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos del usuario no son correctos')
        return self.cleaned_data

