from django.urls import path
from . import views

urlpatterns = [
    path('', views.gastos_list, name='gastos_list'),
    path('gastos/new', views.gastos_new, name='gastos_new'),
    path('gastos/<int:pk>/', views.gastos_detail, name='gastos_detail'),
    path('resumen/', views.resumen, name='resumen'),



]