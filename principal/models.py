from django.db import models
# Create your models here.

'''
(1 punto) CONSTRUIR UN MODELO DE DATOS CORRECTO en Django que almacene la
información siguiente:
a) Anime: Animeid, Título, Géneros, Formato de emisión (TV, movie,…), Número de
episodios.
b) Puntuación: IdUsario, Animeid, Puntuación (1-10)
'''

class Anime(models.Model):
    animeid = models.IntegerField(primary_key=True)
    titulo = models.TextField()
    generos = models.TextField()
    formato = models.TextField()
    episodios = models.IntegerField()

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('titulo', 'animeid', )

class Puntuacion(models.Model):
    idUsuario = models.IntegerField()
    animeid = models.IntegerField()
    puntuacion = models.IntegerField()

    def __str__(self):
        return (str(self.puntuacion))

    class Meta:
        ordering = ('idUsuario', 'animeid', )