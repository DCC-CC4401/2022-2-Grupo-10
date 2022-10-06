from django import forms

from .models import Gastos

class GastosForm(forms.ModelForm):

    class Meta:
        model = Gastos
        fields = [
            'titulo',
            'descripcion',
            'recurrente',
            'fecha_cobro', 
            'prioridad',
            'categoria',
            'monto'
        ]