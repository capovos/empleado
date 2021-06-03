from django.shortcuts import render
from django.urls import reverse_lazy
# Vistas genericas
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView)
# Import Models
from .models import Prueba
from .forms import PruebaForm

# Create your views here.
class PruebaView(TemplateView):
    template_name = "home/home.html"
    
class ResumenFoundationView(TemplateView):
    template_name = "home/resumen_foundation.html"

class PruebaListView(ListView):
    template_name = "home/lista.html"
    context_object_name = 'listaNumeros'
    queryset = ['0','10','20','30']

class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = Prueba
    context_object_name = 'listaPrueba'

class CreatePrueba(CreateView):
    template_name = "home/add_prueba.html"
    model = Prueba
    # fields = ['titulo','subtitulo','cantidad']
    form_class = PruebaForm
    success_url = reverse_lazy('home_app:prueba_lista')