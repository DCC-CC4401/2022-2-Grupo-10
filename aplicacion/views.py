from django.shortcuts import render

# Create your views here.
def gastos_list(request):
    return render(request, 'aplicacion/gastos_list.html', {})