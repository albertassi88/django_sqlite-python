from django.contrib import admin
from .models import Filmes


class AdminFilmes(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'elenco', 'sinopse')


admin.site.register(Filmes, AdminFilmes)


