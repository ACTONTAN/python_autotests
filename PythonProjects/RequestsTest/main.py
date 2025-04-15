import requests

#Создание покемона

URL = 'https://api.pokemonbattle.ru/v2/'
TOKEN = '11273038c632f5fa3c1c495d50adf543'
HEADER = {'Content-Type': 'application/json', 'trainer_token': '11273038c632f5fa3c1c495d50adf543' } 
Body_Create = {
    "name": "Питонавр",
    "photo_id": 1
}
trainer_id = '29013'

qwery_param = trainer_id 

body_add = {
    "pokemon_id": "251025"
} 

body_redact = {
    "pokemon_id": "218913",
    "name": "New Name",
    "photo_id": 2
}

"""response_create = requests.post(url = f'{URL}pokemons', headers = HEADER, json = Body_Create)
print(response_create.text)

message = response_create.json()['message']

print(message)"""

#Изменить покемона

"""requests_redact = requests.put(url = f'{URL}pokemons', headers = HEADER, json = body_redact)
print(requests_redact.text)"""

#Ловим в покебол

requests_add = requests.post(url = f'{URL}trainers/add_pokeball', headers = HEADER, json = body_add)
print(requests_add.text)

# Мои покемоны

"""response_list = requests.get(url = f'{URL}pokemons&{qwery_param}', headers = HEADER, json = ())

print(response_list.text)"""

#Информация о тренере

"""requests_me = requests.get(url = f'{URL}me', headers = HEADER )

print(requests_me.text)

pokemon_id = requests_me.json() ['pokemons_alive']

print(pokemon_id)"""