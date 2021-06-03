from django.shortcuts import render
from django.urls import reverse_lazy
# Vistas genericas
from django.views.generic import (ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView)
# Import Models
from .models import Empleado
from django.views.generic.edit import FormView
# Forms
from .forms import EmpleadoForm


# Create your views here.
class InicioView(TemplateView):
    template_name = "inicio.html"


class PruebaView(ListView):
    template_name = "persona/persona.html"
    model = Empleado
    context_object_name = 'listaEmpleado'


class ListEmpleadosAdmin(ListView):
    template_name = "persona/list_empleados.html"
    paginate_by = 10
    ordering = '-id'
    context_object_name = "empleados"
    model = Empleado


# 1 - Listar todos los empleados de la empresas
class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 5
    ordering = ['-id']
    context_object_name = "empleados"

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(full_name__icontains=palabra_clave)
        return lista

# 2 - Listar todos los empleados q pertenecen a un area de la empresa
class ListByAreaEmpleados(ListView):
    """ Lista Empleados de un Aera filtro por url """
    template_name = "persona/list_by_area.html"
    paginate_by = 5
    context_object_name = "empleados"

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(
            departamento__short_name= area)
        return lista

# 3 - Listar empleados por trabajo


# 4 - Listar los empleados por palabra clave
class ListEmpleadosByKword(ListView):
    """ Lista Empleados de un Aera filtro por Kword """
    template_name = "persona/list_by_kword.html"
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(first_name=palabra_clave)
        return lista

# 5 - Listar habilidades de un empleados
class ListHablidadesEmpleado(ListView):
    """ Lista Habilidades Empleados muchos a muchos"""
    template_name = "persona/habilidades.html"
    context_object_name = 'habilidades'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        empleado = Empleado.objects.get(id=palabra_clave)
        lista = empleado.habilidades.all()
        return lista

# 6 - Detalle empleado
class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['Titulo'] = 'Empleado del mes'
        return context

# 9 - Template Views
class SuccessView(TemplateView):
    template_name = 'persona/success.html'

# 8 - Create view
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add_empleado.html"
    #fields = ('__all__')
    #fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades', 'avatar', 'hoja_vida']
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_list_admin')
    #success_url = '../success/'
    #success_url = '../listar-todo-empleados/'
    #success_url = '.'

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        return super(EmpleadoCreateView, self).form_valid(form)

# 10 - Update View
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "persona/update_empleado.html"
    #fields = ('__all__')
    #fields = ['first_name', 'last_name', 'job', 'departamento', 'habilidades','hoja_vida']
    success_url = reverse_lazy('persona_app:empleados_list_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)

# 11 - Delete Views

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete_empleado.html"
    fields = [
        'first_name', 'last_name', 'job', 'departamento', 'habilidades',
        'hoja_vida'
    ]
    success_url = reverse_lazy('persona_app:empleados_list_admin')
