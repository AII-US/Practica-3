import csv
import os

from principal.models import Anime, Puntuacion, Genero

# Add your auxiliary functions here.
path = os.path.dirname(os.path.abspath(__file__))
def populate_animes():
    path_anime = path + "/data/anime.csv"
    dic = {}
    genero_dic = {}
    Anime.objects.all().delete()
    Genero.objects.all().delete()
    with open(path_anime, "r") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        for anime_id, name, genre, type, episodes in reader:
            if episodes == "Unknown":
                episodes = -1
            else:
                episodes = int(episodes)
            generos = []
            print(generos)
            for nombre_genero in genre.split(","):
                nombre_genero = nombre_genero.strip()
                if genero_dic.get(nombre_genero) == None:
                    genero = Genero.objects.create(nombre=nombre_genero)
                    genero_dic[nombre_genero] = genero
                else:
                    genero = genero_dic[nombre_genero]
                generos.append(genero)
            anime = Anime(animeid=int(anime_id), titulo=name, formato=type, episodios=episodes)
            anime.save()
            anime.generos.set(generos)
            anime.save()
            dic[int(anime_id)] = anime
            anime.save()
    return dic

def populate_ratings(dic):
    path_ratings = path + "/data/ratings.csv"
    ratings = []
    Puntuacion.objects.all().delete()
    with open(path_ratings, "r") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        for user_id, anime_id, rating in reader:
            rating = Puntuacion(idUsuario=int(user_id), animeid=dic[int(anime_id)], puntuacion=int(rating))
            ratings.append(rating)
    Puntuacion.objects.bulk_create(ratings)

def populate_db():
    dic = populate_animes()
    populate_ratings(dic)
    return (Anime.objects.count(), Puntuacion.objects.count())