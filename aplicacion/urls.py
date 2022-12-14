from django.urls import path
from . import views

urlpatterns = [
    path('calendario', views.calendario, name='calendario'),
    path('gastos/new', views.gastos_new, name='gastos_new'),
    path('gastos/<int:pk>/', views.gastos_detail, name='gastos_detail'),
    path('resumen/', views.resumen, name='resumen'),
    path('', views.index, name='index'),


    path('ingresos/new', views.ingresos_new, name='ingresos_new'),
    path('ingresos/<int:pk>/', views.ingresos_detail, name='ingresos_detail'),
    path('register/', views.register, name='register'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('login_user', views.login_user, name='login_user')

]