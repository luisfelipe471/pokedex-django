from unittest.mock import Mock, patch

from django.test import TestCase
from pokedex_app.views import _normalizar_pokemon, TIPOS_PT, STATUS_PT

class NormalizacaoPokemonTests(TestCase):
    def test_traducao_de_tipos_e_atributos(self):
        dados = _normalizar_pokemon({
            'id': 25, 'name': 'pikachu', 'height': 4, 'weight': 60,
            'sprites': {'front_default': 'https://exemplo.test/pikachu.png'},
            'types': [{'type': {'name': 'electric'}}],
            'stats': [{'stat': {'name': 'speed'}, 'base_stat': 90}],
        })
        self.assertEqual(dados['name'], 'Pikachu')
        self.assertEqual(dados['types'], ['Elétrico'])
        self.assertEqual(dados['stats'], [{'nome': 'Velocidade', 'valor': 90}])

    @patch('pokedex_app.views.requests.get')
    def test_busca_pokemon(self, mock_get):
        resposta = Mock(status_code=404)
        mock_get.return_value = resposta
        page = self.client.get('/?nome=desconhecido')
        self.assertContains(page, 'Pokémon não encontrado.')
