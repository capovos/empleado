from django import forms
from django.forms import widgets

from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        model = Prueba
        fields = ('titulo','subtitulo','cantidad',)
        widgets ={
            'titulo': forms.TextInput(
                attrs={
                    'placeholder':'Ingresar titulo',
                    'class':'form-control'
                    })
        }

    
    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        if len(titulo) < 3:
            raise forms.ValidationError(
                'Ingrese un titulo con caracteres mayor a 3')
        return titulo

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        return cantidad
