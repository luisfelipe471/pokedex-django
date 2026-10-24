from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar_pokemon, name='buscar_pokemon'),
    path('lista/', views.listar_pokemons, name='listar_pokemons'),
    path('lista/<int:numero_pagina>/', views.listar_pokemons, name='pagina_pokemons'),
]
