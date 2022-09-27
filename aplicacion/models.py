from django.conf import settings
from django.db import models
from django.utils import timezone


class gastos(models.Model):
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    recurrente = models.CharField(max_length=2)
    fecha_cobro = models.DateField()
    prioridad = models.CharField(max_length=10)
    monto = models.IntegerField()
    categoria = models.CharField(max_length=100)


    def __str__(self):
        return self.titulo