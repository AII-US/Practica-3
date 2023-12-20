from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from .forms import SpinboxListaFormatoForm, UsuarioBusquedaForm, SpinboxListaGeneroForm
from .recommendations import sim_distance, sim_pearson, top_matches, get_recommendations, transform_prefs, calculate_similar_items, get_recommended_items
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Puntuacion, Anime, Genero
import shelve
from django.db.models import Count

from .utils import populate_db


def loadDict():
    Prefs={}
    shelf = shelve.open("dataRS.dat")
    ratings = Puntuacion.objects.all()
    for ra in ratings:
        user = ra.idUsuario
        animeid = ra.animeid.animeid
        rating = ra.puntuacion
        Prefs.setdefault(user, {})
        Prefs[user][animeid] = rating
    shelf['Prefs'] = Prefs
    shelf['ItemsPrefs'] = transform_prefs(Prefs)
    shelf['SimItems'] = calculate_similar_items(Prefs, n=10)
    shelf.close()


def load_data(request):
    (num_anime, num_ratings) = populate_db()
    return render(request, 'load_data.html', context={'message': 'Data loaded successfully: {} anime, {} ratings.'.format(num_anime, num_ratings)})

def load_recommendations(request):
    loadDict()
    # TODO: Llama al método loadRS de utils.py y obtén las entidades de la base de datos para luego mostrarlo.
    return render(request, 'load_recommendations.html', context={'message': 'Recomendaciones cargadas correctamente.'})

def anime_por_formato(request):
    if request.method == 'POST':
        form = SpinboxListaFormatoForm(request.POST)
        if form.is_valid():
            formato_seleccionado = form.cleaned_data['listaFormatos']
            animes = Anime.objects.filter(formato=formato_seleccionado, episodios__gt=5).order_by('episodios')[:5]
            return render(request, 'anime_por_formato.html', context={'animes': animes, 'form': form})
    else:
        form = SpinboxListaFormatoForm()

    return render(request, 'anime_por_formato.html', context={'form': form})

def anime_mas_visto(request):
    top_animes = Anime.objects.annotate(num_puntuaciones=Count('puntuaciones')).order_by('-num_puntuaciones')[:3]
    recommended_animes = {}

    for anime in top_animes:
        recommended_anime_ids = [match[1] for match in
                                 top_matches(transform_prefs(shelve.open("dataRS.dat")['Prefs']), anime.animeid, n=3,
                                             similarity=sim_distance)]
        recommended_animes_for_current = list(Anime.objects.filter(animeid__in=recommended_anime_ids))
        recommended_animes[anime]=(recommended_animes_for_current)

    return render(request, 'anime_mas_visto.html', context={'top_animes': top_animes,'recommended_animes': recommended_animes})


def recomendar_animes(request):
    formulario = SpinboxListaGeneroForm()
    items = None

    if request.method == 'POST':
        formulario = SpinboxListaGeneroForm(request.POST)

        if formulario.is_valid():
            genero = formulario.cleaned_data['listaGeneros']
            idUsuario = formulario.cleaned_data['idUsuario']
            shelf = shelve.open("dataRS.dat")
            Prefs = shelf['Prefs']
            SimItems = shelf['SimItems']
            shelf.close()
            rankings = get_recommended_items(Prefs, SimItems, int(idUsuario))
            animes = []
            puntuaciones = []
            for recomendada in rankings:
                anime = Anime.objects.get(animeid=recomendada[1])
                genero = Genero.objects.get(genero=genero)
                if genero in anime.generos.all():
                    animes.append(anime)
                    puntuaciones.append(recomendada[0])
            items = zip(animes, puntuaciones)
    return render(request,'recomendar_animes.html', context={'items': items, 'formulario': formulario})

def home(request):
    return render(request, 'home.html')

def confirm(request):
    return render(request, 'confirm.html')