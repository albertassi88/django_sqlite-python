from django.urls import path
from .views import menufilmes, filme

urlpatterns = [
    path('', menufilmes, name='menufilmes'),
    path('filmes/<int:pk>', filme, name='filmes'),
]