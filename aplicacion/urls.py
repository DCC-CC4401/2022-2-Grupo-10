from django.urls import path
from . import views

urlpatterns = [
    path('', views.gastos_list, name='gastos_list'),
]