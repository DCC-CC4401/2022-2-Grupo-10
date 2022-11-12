from django import forms

from .models import gastos, Ingresos

class GastosForm(forms.ModelForm):

    class Meta:
        model = gastos
        fields = ('titulo', 'descripcion', 'recurrente', 'fecha_cobro', 'prioridad', 'monto',
        'categoria')

class IngresosForm(forms.ModelForm):

    class Meta:
        model = Ingresos
        fields = ('titulo', 'descripcion', 'recurrente', 'fecha_ingreso', 'monto')