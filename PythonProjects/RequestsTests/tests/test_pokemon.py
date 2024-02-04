import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers_200():
    """
    Get trainers status 200
    """
    response = requests.get(f'{URL}/trainers', timeout=5)
    assert response.status_code == 200, 'Unsuccessful request'

CASES = [
    (3804, 'ananas')
]
@pytest.mark.parametrize('id, trainer_name', CASES)
def test_get_trainers_by_id(id, trainer_name):
    """
    Get trainers by id
    """
    response = requests.get(f'{URL}/trainers', params={'trainer_id': id}, timeout=5)
    assert response.json()['trainer_name'] == trainer_name, 'Wrong trainer'