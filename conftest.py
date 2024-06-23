import random
import string

import pytest
import requests

from Sprint_7.data import COURIER_LOGIN, COURIER


@pytest.fixture(scope='function')
def create_new_courier_and_delete_after_test():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    yield payload

    response = requests.post(COURIER_LOGIN, json={"login": login, "password": password})
    courier_id = response.json().get('id', None)

    requests.delete(f'{COURIER}/{courier_id}')


@pytest.fixture
def order_data():
    return {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }

