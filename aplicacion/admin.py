from django.contrib import admin
from .models import gastos
from .models import Ingresos

admin.site.register(gastos)

admin.site.register(Ingresos)