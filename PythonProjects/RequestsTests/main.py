"""
Pokemon api test
"""

import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': '242d074d8c34f623fc03a2d7f39b7145'}

body = {
    "name": "poki",
    "photo": "https://dolnikov.ru/pokemons/albums/415.png"
}

body1 = {
    "pokemon_id": "29689",
    "name": "poki banana",
    "photo": "https://dolnikov.ru/pokemons/albums/415.png"
}

body2 = {
    "pokemon_id": "29689"
}


response = requests.post(f'{URL}/pokemons', json=body,headers=HEADER, timeout=3)
print(response.text)

response = requests.put(f'{URL}/pokemons', json=body1, headers=HEADER)
print(response.text)

response = requests.post(f'{URL}/trainers/add_pokeball', json=body2, headers=HEADER, timeout=2)
print(response.text)



