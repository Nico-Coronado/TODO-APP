from django.db import models

class TodoManager(models.Manager):
    def listarTareasActuales(self, user):
        l = self.filter(
            user__username=user
        )
        return l
