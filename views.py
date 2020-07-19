from django.shortcuts import render
from .models import Filmes


def menufilmes(request):
    filmes_all = Filmes.objects.all()
    context = {
        'filmes_all': filmes_all
    }

    return render(request, 'menufilmes.html', context)


def filme(request, pk):

    filmeid = Filmes.objects.get(id=pk)

    context = {
        'filmeid': filmeid
    }
    return render(request, 'filmes.html', context)


