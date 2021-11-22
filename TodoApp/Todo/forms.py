from django import  forms

from . models import Todo

class TodoForm(forms.ModelForm):
    """Form definition for Todo."""

    class Meta:
        """Meta definition for Todoform."""

        model = Todo
        fields = ('name', 'description')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }

class TodoUpdateForm(forms.ModelForm):
    """Form definition for Todo."""

    class Meta:
        """Meta definition for Todoform."""

        model = Todo
        fields = ('name','description')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            )
        }


