from django.shortcuts import render
from django.utils import timezone
from .models import Gastos
from django.shortcuts import render, get_object_or_404
from .forms import GastosForm
from django.shortcuts import redirect

# Create your views here.
def gastos_list(request):
    gasto = Gastos.objects.filter(fecha_cobro=timezone.now()).order_by('fecha_cobro')
    return render(request, 'aplicacion/gastos_list.html', {'gasto': gasto})

def gastos_detail(request, pk):
    gasto = get_object_or_404(Gastos, pk=pk)
    return render(request, 'aplicacion/gastos_detail.html', {'gastos': gastos})

def gastos_new(request):
    if request.method == "POST":
        form = GastosForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            form.author = request.user
            form.published_date = timezone.now()
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            recurrente = request.POST['recurrente']
            fecha_cobro = request.POST['fecha_cobro']
            prioridad = request.POST['prioridad']
            categoria = request.POST['categoria']
            monto = request.POST['monto']
            return redirect('gastos_detail', pk=gasto.pk)
    else:
        form = GastosForm()
    
    return render(request, 'aplicacion/gastos_edit.html', {'form': form})