import requests
from django.core.paginator import Paginator
from django.shortcuts import render

TIPOS_PT = {
    'normal': 'Normal', 'fire': 'Fogo', 'water': 'Água',
    'electric': 'Elétrico', 'grass': 'Planta', 'ice': 'Gelo',
    'fighting': 'Lutador', 'poison': 'Veneno', 'ground': 'Terra',
    'flying': 'Voador', 'psychic': 'Psíquico', 'bug': 'Inseto',
    'rock': 'Pedra', 'ghost': 'Fantasma', 'dragon': 'Dragão',
    'dark': 'Sombrio', 'steel': 'Aço', 'fairy': 'Fada',
}

STATUS_PT = {
    'hp': 'Vida', 'attack': 'Ataque', 'defense': 'Defesa',
    'special-attack': 'Ataque Especial',
    'special-defense': 'Defesa Especial', 'speed': 'Velocidade',
}

def _traduzir_valor(valor, mapa):
    if not valor:
        return ''
    valor_normalizado = valor.lower().strip()
    if valor_normalizado in mapa:
        return mapa[valor_normalizado]
    return valor_normalizado.replace('-', ' ').replace('_', ' ').capitalize()

def _normalizar_pokemon(dados):
    if not dados:
        return None
    tipos = [
        _traduzir_valor(tipo.get('type', {}).get('name', ''), TIPOS_PT)
        for tipo in dados.get('types', [])
        if tipo.get('type', {}).get('name')
    ]
    stats = []
    for stat in dados.get('stats', []):
        nome = stat.get('stat', {}).get('name', '')
        valor = stat.get('base_stat')
        if nome and valor is not None:
            stats.append({
                'nome': _traduzir_valor(nome, STATUS_PT),
                'valor': valor,
            })
    return {
        'id': dados.get('id'),
        'name': dados.get('name', '').capitalize(),
        'height': dados.get('height'),
        'weight': dados.get('weight'),
        'sprites': dados.get('sprites', {}),
        'types': tipos,
        'stats': stats,
    }

def buscar_pokemon(request):
    nome = request.GET.get('nome', '').strip().lower()
    dados, erro = None, None
    if nome:
        try:
            resposta = requests.get(
                f'https://pokeapi.co/api/v2/pokemon/{requests.utils.quote(nome, safe="")}',
                timeout=12,
            )
            if resposta.status_code == 200:
                dados = _normalizar_pokemon(resposta.json())
            else:
                erro = 'Pokémon não encontrado.'
        except (requests.RequestException, ValueError):
            erro = 'Não foi possível consultar a PokéAPI. Tente novamente.'
    return render(request, 'pokedex_app/pokemon.html', {'dados': dados, 'erro': erro})

def listar_pokemons(request, numero_pagina=1):
    erro = None
    pokemons = []
    try:
        resposta = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1000', timeout=12)
        resposta.raise_for_status()
        pokemons = resposta.json().get('results', [])
    except (requests.RequestException, ValueError):
        erro = 'Não foi possível carregar a lista de Pokémon.'
    paginador = Paginator(pokemons, 10)
    pagina = paginador.get_page(numero_pagina)
    return render(request, 'lista.html', {'pagina': pagina, 'erro': erro})
