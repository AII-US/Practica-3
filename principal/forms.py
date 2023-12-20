# encoding:utf-8
from django import forms

from principal.models import Anime
class SpinboxListaFormatoForm(forms.Form):
    formatos = set(Anime.objects.values_list('formato', 'formato').distinct())
    listaFormatos = forms.ChoiceField(label="Formato", widget=forms.Select, choices=formatos, required=True)

class SpinboxIdUsuarioForm(forms.Form):
    idUsuario = forms.ChoiceField(label="Id de Usuario", widget=forms.NumberInput, required=True)