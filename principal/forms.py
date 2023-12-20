# encoding:utf-8
from django import forms


class UsuarioBusquedaForm(forms.Form):
    idUsuario = forms.CharField(label="Id de Usuario", widget=forms.TextInput, required=True)


class PeliculaBusquedaForm(forms.Form):
    idPelicula = forms.CharField(label="Id de Pelicula", widget=forms.TextInput, required=True)

class SpinboxIdUsuarioForm(forms.Form):
    idUsuario = forms.IntegerField(label="Id de Usuario", widget=forms.NumberInput, required=True, min_value=1, max_value=943)