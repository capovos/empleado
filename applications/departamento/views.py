from django.shortcuts import render
from django.urls import reverse_lazy
# Vistas genericas
from django.views.generic import (ListView, DetailView, CreateView,
                                  TemplateView, UpdateView, DeleteView)
from django.views.generic.edit import FormView

from .forms import NewDepartamentoForm
from .models import Departamento
from applications.persona.models import Empleado

# Create your views here.
class DepartamentoListView(ListView):
    template_name = "departamento/list_all.html"
    paginate_by = 4
    ordering_by = "short_name"
    context_object_name = "departamento"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Departamento.objects.filter(name__icontains=palabra_clave)
        return lista


class NewDepartamento(FormView):
    template_name = "departamento/add_departamento.html"
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('departamento_app:departamento_list')

    def form_valid(self, form):
        depa = Departamento(name=form.cleaned_data['departamento'],
                            short_name=form.cleaned_data['shortname'])
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        Empleado.objects.create(first_name=nombre, last_name=apellido,job='1',departamento=depa)


        return super(NewDepartamento, self).form_valid(form)