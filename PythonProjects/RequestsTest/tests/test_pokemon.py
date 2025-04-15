import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '11273038c632f5fa3c1c495d50adf543'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '11273038c632f5fa3c1c495d50adf543' } 
trainer_id = '29013'
def test_status_code():
    response = requests.get(url = f'{URL}pokemons',params = {'trainer_id': trainer_id})
    assert response.status_code == 200