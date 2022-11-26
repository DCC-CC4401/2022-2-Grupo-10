from django.contrib import admin
from .models import gastos
from .models import ingresos

admin.site.register(gastos)

admin.site.register(ingresos)