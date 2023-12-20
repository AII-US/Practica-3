import csv

from principal.models import Anime, Puntuacion


# Add your auxiliary functions here.
path = "data"
def populate_animes():
    path_anime = path + "\\animes.csv"
    animes = []
    dic = {}
    with open(path_anime, "r") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        for anime_id, name, genre, type, episodes in reader:
            if episodes == "Unknown":
                episodes = -1
            else:
                episodes = int(episodes)
            anime = Anime(animeid=int(anime_id), titulo=name, generos=genre, formato=type, episodios=episodes)
            dic[int(anime_id)] = anime
            animes.append(anime)
    Anime.objects.bulk_create(animes)
    return dic

def populate_ratings(dic):
    path_ratings = path + "\\ratings.csv"
    ratings = []
    with open(path_ratings, "r") as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        for user_id, anime_id, rating in reader:
            rating = Puntuacion(idUsuario=int(user_id), animeid=dic[int(anime_id)], rating=int(rating))
            ratings.append(rating)
    Puntuacion.objects.bulk_create(ratings)

def populate_db():
    dic = populate_animes()
    populate_ratings(dic)
    return (Anime.objects.count(), Puntuacion.objects.count())