from django import forms

from .models import Departamento


class NewDepartamentoForm(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    apellido = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    departamento = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    shortname = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )