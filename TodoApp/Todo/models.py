from django.db import models
from django.contrib.auth.models import User

from . managers import TodoManager

class Todo(models.Model):
    name = models.CharField("Nombre" ,max_length=20)
    description = models.CharField("Descripcion", max_length=100)
    user = models.ForeignKey(User, verbose_name="Usuario", on_delete=models.CASCADE)
    create_at = models.DateTimeField("Creado el", auto_now_add=True)
    update_at = models.DateTimeField("Actualizado el", auto_now=True)

    objects = TodoManager()

    class Meta:
        ordering = ['create_at']

    def __str__(self):
        return self.name

