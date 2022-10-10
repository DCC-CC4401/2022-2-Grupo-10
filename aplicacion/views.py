from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import gastos
from .forms import GastosForm


# Create your views here.
def gastos_list(request):
    gastos_o = gastos.objects.all()
    return render(request, 'aplicacion/inicio.html', {'gastos_o' :gastos_o})


def gastos_detail(request, pk):
    gastos_a = get_object_or_404(gastos, pk=pk)
    return render(request, 'aplicacion/gastos_detail.html', {'gastos_a': gastos_a})



def gastos_new(request):
    form = GastosForm()
    if request.method == "POST":
        form = GastosForm(request.POST)
        if form.is_valid():
            gastos = form.save(commit=False)
            gastos.id_usuario = request.user
            gastos.save()
            return redirect('gastos_detail', pk=gastos.pk)


    else:
        form = GastosForm()
    return render(request, 'aplicacion/GastosForm.html', {'form': form})


def resumen(request):
    if request.method == 'GET':
        gastos_o = gastos.objects.all()
        # e = request.GET.get('data-range') Esto debería obtener la opción escogida en el select
        final_date = timezone.now()
        init_date_1 = timezone.now().date() - timedelta(days=7)
        init_date_2 = timezone.now().date() - timedelta(days=30)
        init_date_3 = timezone.now().date() - timedelta(days=60)
        gastos1 = gastos.objects.filter(fecha_cobro__range=[init_date_1, final_date]) #Tabla opción 1
        gastos2 = gastos.objects.filter(fecha_cobro__range=[init_date_2, final_date]) #Tabla opción 2
        gastos3 = gastos.objects.filter(fecha_cobro__range=[init_date_3, final_date]) #Tabla opción 
        return render(request, 'aplicacion/resumen.html', {'gastos_o': gastos2, # Este es el valor default
                        'gastos1' :gastos1, 'gastos2': gastos2, 'gastos3': gastos3})
