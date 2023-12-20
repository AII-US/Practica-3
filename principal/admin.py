from django.contrib import admin

from principal.models import Anime, Puntuacion

# Register your models here.

admin.site.register([Anime, Puntuacion])