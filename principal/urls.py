from django.urls import path
from django.contrib import admin

from principal.views import load_data, home, load_recommendations, login_petition, confirm, anime_por_formato, \
    anime_mas_visto, recomendar_anime

# Add your URLs here.

urlpatterns = [
    path('login/', login_petition, name='login'),
    path('home/', home, name='home'),
    path('', home, name='home'),
    path('load_db/', load_data, name='load_db'),
    path('load_recommendations/', load_recommendations, name='load_recommendations'),
    path('confirm/', confirm, name='confirm'),
    path('anime_por_formato/', anime_por_formato, name='anime_por_formato'),
    path('anime_mas_visto/', anime_mas_visto, name='anime_mas_visto'),
    path('recomendar_anime/', recomendar_anime, name='recomendar_anime')
]