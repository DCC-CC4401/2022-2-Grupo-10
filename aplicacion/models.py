from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.admin import widgets 


class gastos(models.Model):
    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)
    RECURRENCIA = [
        ('Si', 'Si'),
        ('No', 'No'),
    ]
    recurrente = models.CharField(max_length=2, choices=RECURRENCIA)
    fecha_cobro = models.DateField()
    PRIORIDAD = [
        ('Alta', 'Alta'),
        ('Media', 'Media'),
        ('Baja', 'Baja'), 
    ]
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD)
    monto = models.IntegerField()
    CATEGORIA = [
        ('Entretención', 'Entretención'),
        ('Transporte', 'Transporte'),
        ('Alimento', 'Alimentos'),
        ('Cuentas Básicas', 'Cuentas Básicas'),
        ('Dividendo', 'Dividendo'),
        ('Otros', 'Otros'),
    ]
    categoria = models.CharField(max_length=100, choices=CATEGORIA)


    def __str__(self):
        return self.titulo

class Meta:
    ordering = ["-fecha"]