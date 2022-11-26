from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from datetime import timedelta
from .models import ingresos, gastos
from django.db.models import Sum
# from django.contrib.auth.decorators import login_required
from .forms import GastosForm, IngresosForm, RegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])    
    else:
        form = RegisterForm()

    return render(request, 'aplicacion/registro.html', {'form':form})

def gastos_list(request):
    gastos_o = gastos.objects.all()
    ingresos_o = ingresos.objects.all()
    return render(request, 'aplicacion/inicio.html', {'gastos_o' :gastos_o, 'ingresos_o' :ingresos_o})


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

###Ingresos###
def ingresos_list(request):
    ingresos_o = ingresos.objects.all()
    return render(request, 'aplicacion/inicio.html', {'ingresos_o' :ingresos_o})


def ingresos_detail(request, pk):
    ingresos_a = get_object_or_404(ingresos, pk=pk)
    return render(request, 'aplicacion/ingresos_detail.html', {'ingresos_a': ingresos_a})


def ingresos_new(request):
    form = IngresosForm()
    if request.method == "POST":
        form = IngresosForm(request.POST)
        if form.is_valid():
            ingresos = form.save(commit=False)
            ingresos.id_usuario = request.user
            ingresos.save()
            return redirect('ingresos_detail', pk=ingresos.pk)


    else:
        form = IngresosForm()
    return render(request, 'aplicacion/IngresosForm.html', {'form': form})

################################################################
# Resumen general (funcionando)
################################################################

def filtro_tablas():
    final_date = timezone.now()
    init_date_1 = timezone.now().date() - timedelta(days=7)
    init_date_2 = timezone.now().date() - timedelta(days=30)
    init_date_3 = timezone.now().date() - timedelta(days=60)

    year = final_date.year

    gastos1 = gastos.objects.order_by('fecha_cobro').filter(fecha_cobro__range=[init_date_1, final_date]) #Tabla opción 1
    gastos2 = gastos.objects.order_by('fecha_cobro').filter(fecha_cobro__range=[init_date_2, final_date]) #Tabla opción 2
    gastos3 = gastos.objects.order_by('fecha_cobro').filter(fecha_cobro__range=[init_date_3, final_date]) #Tabla opción 3
    gastoanual = gastos.objects.order_by('fecha_cobro').filter(fecha_cobro__year__gte=year, fecha_cobro__month__gte=1, fecha_cobro__day__gte=1, 
                fecha_cobro__lte=final_date) # Tabla opción 4
    return (gastos1, gastos2, gastos3, gastoanual)

def filtro_tablas_ingresos():
    final_date = timezone.now()
    init_date_1 = timezone.now().date() - timedelta(days=7)
    init_date_2 = timezone.now().date() - timedelta(days=30)
    init_date_3 = timezone.now().date() - timedelta(days=60)

    year = final_date.year

    ingresos1 = ingresos.objects.order_by('fecha_ingreso').filter(fecha_ingreso__range=[init_date_1, final_date]) #Tabla opción 1
    ingresos2 = ingresos.objects.order_by('fecha_ingreso').filter(fecha_ingreso__range=[init_date_2, final_date]) #Tabla opción 2
    ingresos3 = ingresos.objects.order_by('fecha_ingreso').filter(fecha_ingreso__range=[init_date_3, final_date]) #Tabla opción 3
    ingresoanual = ingresos.objects.order_by('fecha_ingreso').filter(fecha_ingreso__year__gte=year, fecha_ingreso__month__gte=1, fecha_ingreso__day__gte=1,
                                                                     fecha_ingreso__lte=final_date) # Tabla opción 4
    return (ingresos1, ingresos2, ingresos3, ingresoanual)

def pie_chart_resumen():
    sum_ent = gastos.objects.filter(categoria='Entretención').aggregate(Sum('monto'))['monto__sum']
    sum_tr = gastos.objects.filter(categoria='Transporte').aggregate(Sum('monto'))['monto__sum']
    sum_al = gastos.objects.filter(categoria='Alimento').aggregate(Sum('monto'))['monto__sum']
    sum_cb = gastos.objects.filter(categoria='Cuentas Básicas').aggregate(Sum('monto'))['monto__sum']
    sum_div = gastos.objects.filter(categoria='Dividendo').aggregate(Sum('monto'))['monto__sum']
    sum_ot = gastos.objects.filter(categoria='Otros').aggregate(Sum('monto'))['monto__sum']

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
        ingresos =ingresos.objects.filter(fecha_ingreso__year__gte=year,  # Luego gastos se reemplazará por ingresos
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
    
    ingresos =ingresos.objects.filter(fecha_ingreso__year__gte=year,  # Luego gastos se reemplazará por ingresos
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
        (ingresos1, ingresos2, ingresos3, ingresoanual) = filtro_tablas_ingresos()
        (cat_list, number_list) = pie_chart_resumen()
        (name_d_list, date_list, date_list_2) = bar_chart_resumen()
        diccionario = {'gastos1' :gastos1, 'gastos2': gastos2, 'gastos3': gastos3, 'gastoanual': gastoanual,
                        'ingresos1' :ingresos1, 'ingresos2': ingresos2, 'ingresos3': ingresos3, 'ingresoanual': ingresoanual, 
                        'cat_list': cat_list, 'number_list': number_list, 
                        'name_d_list': name_d_list, 'date_list': date_list, 'date_list_2': date_list_2}
        return render(request, 'aplicacion/resumen_html/resumen.html', diccionario)



