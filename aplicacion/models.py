from django.conf import settings
from django.db import models
from django.utils import timezone


class Gastos(models.Model):
    #id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    RECURRENCIA = (
        ('Si','Si es recurrente'),
        ('No','No es recurrente'),
    )
    recurrente = models.CharField(max_length=2, choices=RECURRENCIA)
    fecha_cobro = models.DateField()
    PRIORIDAD = (
        ('Alta', 'Alta priorida'),
        ('Media', 'Media prioridad'),
        ('Baja', 'Baja prioridad'),
    )
    prioridad = models.CharField(max_length=5, choices=PRIORIDAD)
    CATEGORIA = (
        ('Entretención', 'Gasto en entretención'),
        ('Transporte', 'Gasto en transporte'),
        ('Alimento', 'Gasto en Alimentos'),
        ('Cuentas Básicas', 'Gastos en cuentas Básicas'),
        ('Dividendo', 'Gatos en dividendo')
    )
    categoria = models.CharField(max_length=20, choices=CATEGORIA)
    monto = models.IntegerField()


    def __str__(self):
        return self.titulo