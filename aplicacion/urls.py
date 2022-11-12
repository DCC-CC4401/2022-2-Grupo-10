from django.urls import path
from . import views

urlpatterns = [
    path('', views.gastos_list, name='gastos_list'),
    path('gastos/new', views.gastos_new, name='gastos_new'),
    path('gastos/<int:pk>/', views.gastos_detail, name='gastos_detail'),
    path('resumen/', views.resumen, name='resumen'),

    ##############################################
    ############ path para ingresos ##############

    path('', views.ingresos_list, name='ingresos_list'),
    path('ingresos/new', views.ingresos_new, name='ingresos_new'),
    path('ingresos/<int:pk>/', views.ingresos_detail, name='ingresos_detail'),

]