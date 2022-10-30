from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Ingresos, gastos
# from django.contrib.auth.decorators import login_required
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


################################################################
# Resumen general (funcionando)
################################################################

def filtro_tablas():
    final_date = timezone.now()
    init_date_1 = timezone.now().date() - timedelta(days=7)
    init_date_2 = timezone.now().date() - timedelta(days=30)
    init_date_3 = timezone.now().date() - timedelta(days=60)

    year = final_date.year
    month = final_date.month
    day = final_date.day

    gastos1 = gastos.objects.order_by('fecha_cobro').filter(fecha_cobro__range=[init_date_1, final_date]) #Tabla opción 1
    gastos2 = gastos.objects.order_by('fecha_cobro').filter(fecha_cobro__range=[init_date_2, final_date]) #Tabla opción 2
    gastos3 = gastos.objects.order_by('fecha_cobro').filter(fecha_cobro__range=[init_date_3, final_date]) #Tabla opción 3
    gastoanual = gastos.objects.order_by('fecha_cobro').filter(fecha_cobro__year__gte=year, fecha_cobro__month__gte=1, fecha_cobro__day__gte=1, 
                fecha_cobro__year__lte=year, fecha_cobro__month__lte=month, fecha_cobro__day__lte=day) # Tabla opción 4
    return (gastos1, gastos2, gastos3, gastoanual)

def pie_chart_resumen():
    sum_ent = int(gastos.objects.filter(categoria='Entretención').count())
    sum_tr = int(gastos.objects.filter(categoria='Transporte').count())
    sum_al = int(gastos.objects.filter(categoria='Alimento').count())
    sum_cb = int(gastos.objects.filter(categoria='Cuentas Básicas').count())
    sum_div = int(gastos.objects.filter(categoria='Dividendo').count())
    sum_ot = int(gastos.objects.filter(categoria='Otros').count())

    cat_list = ['Entretención', 'Transporte', 'Alimento', 'Cuentas Básicas', 'Dividendo', 'Otros']
    number_list = [sum_ent, sum_tr, sum_al, sum_cb, sum_div, sum_ot]
    return (cat_list, number_list)

def bar_chart_resumen():
    final_date = timezone.now()
    year = final_date.year
    actual_month = final_date.month
    today = final_date.day
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']  
    name_d_list = meses[:actual_month]

    date_list = []
    date_list_2 = []
    filter_month=1
    while(filter_month<actual_month):
        gastos2 =gastos.objects.filter(fecha_cobro__year__gte=year,
                                fecha_cobro__month__gte=filter_month,
                              fecha_cobro__year__lte=year,
                              fecha_cobro__month__lte=filter_month) 
        total = 0
        for i in range(len(gastos2)):
            total+=gastos2[i].monto

        date_list.append(total)
        ###########################################################
        # Lo mismo pero para ingresos
        ###########################################################
        ingresos =Ingresos.objects.filter(fecha_ingreso__year__gte=year, # Luego gastos se reemplazará por ingresos
                                fecha_ingreso__month__gte=filter_month,
                              fecha_ingreso__year__lte=year,
                              fecha_ingreso__month__lte=filter_month) 
        total2 = 0
        for i in range(len(ingresos)):
            total2+=ingresos[i].monto

        date_list_2.append(total2)
        
        filter_month+=1

    gastos2 =gastos.objects.filter(fecha_cobro__year__gte=year,
                                fecha_cobro__month__gte=filter_month,
                                fecha_cobro__day__gte=1,
                              fecha_cobro__year__lte=year,
                              fecha_cobro__month__lte=filter_month,
                              fecha_cobro__day__lte = today) 
    total = 0
    for i in range(len(gastos2)):
        total+=gastos2[i].monto
    date_list.append(total)
    
    ingresos =Ingresos.objects.filter(fecha_ingreso__year__gte=year, # Luego gastos se reemplazará por ingresos
                                fecha_ingreso__month__gte=filter_month,
                                fecha_ingreso__day__gte=1,
                              fecha_ingreso__year__lte=year,
                              fecha_ingreso__month__lte=filter_month,
                              fecha_ingreso__day__lte = today) 
    total2 = 0
    for i in range(len(ingresos)):
        total2+=ingresos[i].monto
    date_list_2.append(total2)
    
    return (name_d_list, date_list, date_list_2)

def resumen(request):
    if request.method == 'GET':
        (gastos1, gastos2, gastos3, gastoanual) = filtro_tablas()
        (cat_list, number_list) = pie_chart_resumen()
        (name_d_list, date_list, date_list_2) = bar_chart_resumen()
        diccionario = {'gastos1' :gastos1, 'gastos2': gastos2, 'gastos3': gastos3, 'gastoanual': gastoanual, 'cat_list': cat_list, 
                        'number_list': number_list, 'name_d_list': name_d_list, 'date_list': date_list, 'date_list_2': date_list_2}
        return render(request, 'aplicacion/resumen.html', diccionario)