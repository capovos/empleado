from django import forms

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ('first_name', 'last_name', 'job', 'departamento', 'habilidades','avatar','hoja_vida')

        widgets = {
            'first_name':
            forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':
            forms.TextInput(attrs={'class': 'form-control'}),
            'job':
            forms.Select(attrs={'class': 'form-control'}),
            'departamento':
            forms.Select(attrs={'class': 'form-control'}),
            'habilidades':
            forms.SelectMultiple(attrs={'class': 'form-control'}),
            'avatar':
            forms.FileInput(attrs={'class': 'form-control'}),
            'hoja_vida':
            forms.Textarea(attrs={
                'class': 'form-control'
            }),
        }