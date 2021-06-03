from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('lista-prueba/', views.ListarPrueba.as_view(), name='prueba_lista'),
    path('add-prueba/', views.CreatePrueba.as_view(), name='prueba_add'),
    path('resumen-foundation/', views.ResumenFoundationView.as_view(), name='resumen_foundation'),
]