import requests
import pytest

def test_status_code():
    token = "4653e43a2009035cec673af0dcb9ee15"
    response = requests.get('https://api.pokemonbattle.me:9104/trainers', headers={'trainer_token' : token}, json={
        "trainer_id": 1172
    })
    assert response.status_code ==200