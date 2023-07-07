import requests

token = "4653e43a2009035cec673af0dcb9ee15"

base_url = 'https://api.pokemonbattle.me:9104/'

response_add_pokemon = requests.post(f'{base_url}pokemons', headers={'trainer_token' : token}, json ={
    "name": "Тинки",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print(response_add_pokemon.text)

response_rename_pokemon = requests.put(f'{base_url}pokemons', headers={'trainer_token' : token}, json ={
    "pokemon_id": "1599",
    "name": "Хрякозавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print(response_rename_pokemon.text)

response_add_pokeball = requests.post(f'{base_url}trainers/add_pokeball', headers={'trainer_token' : token}, json ={
    "pokemon_id": "1600"
})

print(response_add_pokeball.text)