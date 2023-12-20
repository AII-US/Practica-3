from django.db import models
# Create your models here.
class Genero(models.Model):
    nombre = models.TextField(unique=True)

    def __str__(self):
        return self.nombre

class Anime(models.Model):
    animeid = models.IntegerField(primary_key=True)
    titulo = models.TextField()
    generos = models.ManyToManyField(Genero, related_name='generos')
    formato = models.TextField()
    episodios = models.IntegerField()

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ('titulo', 'animeid', )

class Puntuacion(models.Model):
    idUsuario = models.IntegerField()
    animeid = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='puntuaciones')
    puntuacion = models.IntegerField()

    def __str__(self):
        return (str(self.puntuacion))

    class Meta:
        ordering = ('idUsuario', 'animeid', )