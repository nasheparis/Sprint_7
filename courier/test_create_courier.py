import allure
import requests

from Sprint_7.data import COURIER


class TestCreateCourier:
    @allure.title("Тест проверяет успешное создание курьера")
    def test_create_courier_positive(self, create_new_courier_and_delete_after_test):
        payload = create_new_courier_and_delete_after_test
        response = requests.post(COURIER, json=payload)
        assert response.status_code == 201 and response.json() == {"ok": True}

    @allure.title("Тест проверяет, что нельзя создать курьера, не указав обязательные поля")
    def test_create_courier_missing_required_data(self):
        data = {
            "firstName": "courier007"
        }
        response = requests.post(COURIER, json=data)
        assert response.status_code == 400 and response.json()[
            "message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Тест проверяет, что нельзя создать курьера, не указав хотя бы одно обязательное поле")
    def test_create_courier_missing_required_password(self):
        data = {
            "login": "courier007"
        }
        response = requests.post(COURIER, json=data)
        assert response.status_code == 400 and response.json()[
            "message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Тест проверяет, что поле 'firstName' не обязательно для создания курьера")
    def test_create_courier_missing_optional_data(self, create_new_courier_and_delete_after_test):
        payload = create_new_courier_and_delete_after_test.copy()
        payload.pop('firstName', None)
        response = requests.post(COURIER, json=payload)
        assert response.status_code == 201 and response.json() == {"ok": True}

    @allure.title("Тест проверяет, что нельзя создать два одинаковых курьера")
    def test_create_courier_duplicate_login(self, create_new_courier_and_delete_after_test):
        payload = create_new_courier_and_delete_after_test
        requests.post(COURIER, json=payload)
        response = requests.post(COURIER, json=payload)
        assert response.status_code == 409 and response.json()[
            "message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Тест проверяет, что нельзя создать курьера, отправив пустое поле запроса")
    def test_create_courier_empty_request_body(self):
        data = {}
        response = requests.post(COURIER, json=data)
        assert response.status_code == 400 and response.json()[
            "message"] == "Недостаточно данных для создания учетной записи"
