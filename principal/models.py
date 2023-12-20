from django.db import models
# Create your models here.
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
    animeid = models.ForeignKey(Anime, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()

    def __str__(self):
        return (str(self.puntuacion))

    class Meta:
        ordering = ('idUsuario', 'animeid', )