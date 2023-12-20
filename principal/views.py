from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .recommendations import sim_distance, sim_pearson, top_matches, get_recommendations, transform_prefs, calculate_similar_items, get_recommended_items
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Puntuacion, Anime
import shelve

from .utils import populate_db


def loadDict():
    Prefs={}
    shelf = shelve.open("dataRS.dat")
    ratings = Puntuacion.objects.all()
    for ra in ratings:
        user = ra.idusuario.idUsuario
        animeid = ra.animeid.animeid
        rating = ra.puntuacion
        Prefs.setdefault(user, {})
        Prefs[user][animeid] = rating
    shelf['Prefs']=Prefs
    shelf['ItemsPrefs']=transform_prefs(Prefs)
    shelf.close()


def load_data(request):
    (num_anime, num_ratings) = populate_db()
    return render(request, 'load_data.html', context={'message': 'Data loaded successfully: {} anime, {} ratings.'.format(num_anime, num_ratings)})

def load_recommendations(request):
    loadDict()
    # TODO: Llama al método loadRS de utils.py y obtén las entidades de la base de datos para luego mostrarlo.
    return render(request, 'load_recommendations.html', context={'message': 'Recommendations loaded successfully.'})

def anime_por_formato(request):
    return render(request, 'anime_por_formato.html')

def anime_mas_visto(request):
    return render(request, 'anime_mas_visto.html')

def recomendar_anime(request):
    return render(request, 'recomendar_anime.html')

def home(request):
    return render(request, 'home.html')

def confirm(request):
    return render(request, 'confirm.html')