from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'job',
        'departamento',
        'full_name'
    )
    # Funciones
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name
    # Filtros y search
    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'habilidades')
    # Campos muchos a muchos
    filter_horizontal = ('habilidades',)
admin.site.register(Empleado, EmpleadoAdmin)