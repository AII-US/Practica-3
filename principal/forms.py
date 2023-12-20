# encoding:utf-8
from django import forms

from principal.models import Anime


class UsuarioBusquedaForm(forms.Form):
    idUsuario = forms.CharField(label="Id de Usuario", widget=forms.TextInput, required=True)


class PeliculaBusquedaForm(forms.Form):
    idPelicula = forms.CharField(label="Id de Pelicula", widget=forms.TextInput, required=True)

'''
Muestre un formulario con un una spinbox con
la lista de formatos que hay en la BD. Cuando se seleccione un formato muestra el total
de animes de ese formato con más de 5 episodios ordenados por número de episodios'''
class SpinboxListaFormatoForm(forms.Form):
    formatos = set(Anime.objects.values_list('formato', 'formato').distinct())
    listaFormatos = forms.ChoiceField(label="Formato", widget=forms.Select, choices=formatos, required=True)

class SpinboxIdUsuarioForm(forms.Form):
    idUsuario = forms.ChoiceField(label="Id de Usuario", widget=forms.NumberInput, required=True)