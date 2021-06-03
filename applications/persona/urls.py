from django.contrib import admin
from django.urls import path
from . import views

app_name = "persona_app"

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('prueba/', views.PruebaView.as_view()),
    path('listar-todo-empleados/',
         views.ListAllEmpleados.as_view(),
         name='empleados_all'),
    path('listar-empleados-admin/',
         views.ListEmpleadosAdmin.as_view(),
         name='empleados_list_admin'),
    path('listar-by-area/<shortname>/',
         views.ListByAreaEmpleados.as_view(),
         name='empleado_por_area'),
    path('buscar-empleado/', views.ListEmpleadosByKword.as_view()),
    path('listar-habilidades/', views.ListHablidadesEmpleado.as_view()),
    path('ver-empleado/<pk>/',
         views.EmpleadoDetailView.as_view(),
         name='empleado_detail'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(),name='empleado_add'),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(),name='empleado_update'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='empleado_delete'),
]