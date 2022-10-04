from django import forms

from .models import gastos

class GastosForm(forms.ModelForm):

    class Meta:
        model = gastos
        fields = ('titulo', 'descripcion', 'recurrente', 'fecha_cobro', 'prioridad', 'monto',
        'categoria')

