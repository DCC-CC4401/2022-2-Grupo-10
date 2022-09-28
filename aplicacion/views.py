from django.shortcuts import render
from django.utils import timezone
from .models import gastos

# Create your views here.
def gastos_list(request):
    gastos_o = gastos.objects.filter(fecha_cobro=timezone.now()).order_by('fecha_cobro')

    return render(request, 'aplicacion/gastos_list.html', {'gastos_o' :gastos_o})