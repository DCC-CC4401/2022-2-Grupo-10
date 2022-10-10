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
    gast = get_object_or_404(gastos, pk=pk)
    return render(request, 'aplicacion/gastos_detail.html', {'gast': gast})



def gastos_new(request):
    form = GastosForm()
    if request.method == "POST":
        form = GastosForm(request.POST)
        if form.is_valid():
            gastos = form.save(commit=False)
            gastos.id_usuario = request.user
            gastos.fecha_cobro = timezone.now()
            gastos.save()
            return redirect('gastos_detail', pk=gastos.pk)


    else:
        form = GastosForm()
    return render(request, 'aplicacion/GastosForm.html', {'form': form})


def resumen(request):
    if request.method == 'GET':
        gastos_o = gastos.objects.all()
        e = request.POST.get('data-range')
        final_date = timezone.now()
        init_date = timezone.now().date() - timedelta(days=7) #Default
        if (e == "1"):
            init_date = timezone.now().date() - timedelta(days=7)
        elif (e == "2"):
            init_date = timezone.now().date() - timedelta(days=30)
        elif (e == "3"):
            init_date = timezone.now().date() - timedelta(days=60)
        gastos_o = gastos.objects.filter(fecha_cobro__range=[init_date, final_date])
        return render(request, 'aplicacion/resumen.html', {'gastos_o' :gastos_o, 'final_date': final_date, 'init_date': e})
    else:
        gastos_o = gastos.objects.all()
        return render(request, 'aplicacion/resumen.html', {'gastos_o' :gastos_o})

