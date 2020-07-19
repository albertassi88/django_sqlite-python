from django.db import models


class Filmes(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=40)
    elenco = models.CharField(max_length=60)
    sinopse = models.CharField(max_length=1400)

    def __str__(self):
        return self.titulo



