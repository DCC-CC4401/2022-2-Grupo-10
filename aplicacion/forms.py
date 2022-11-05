from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import gastos

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class GastosForm(forms.ModelForm):

    class Meta:
        model = gastos
        fields = ('titulo', 'descripcion', 'recurrente', 'fecha_cobro', 'prioridad', 'monto',
        'categoria')

