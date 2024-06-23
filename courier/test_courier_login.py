import allure
import requests

from Sprint_7.data import COURIER_LOGIN, COURIER


class TestCourierLogin:
    @allure.title("Тест проверяет успешный логин курьера")
    def test_courier_login_positive(self, create_new_courier_and_delete_after_test):
        data = create_new_courier_and_delete_after_test
        requests.post(COURIER, json=data)
        response = requests.post(COURIER_LOGIN, json={"login": data['login'], "password": data['password']})
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title("Тест проверяет, что курьер не может авторизоваться, не указав обязательные поля")
    def test_courier_login_missing_required_fields(self, create_new_courier_and_delete_after_test):
        data = create_new_courier_and_delete_after_test
        requests.post(COURIER, json=data)
        response = requests.post(COURIER_LOGIN, json={"password": data['password']})
        assert response.status_code == 400 and response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Тест проверяет, что курьер не может авторизоваться, если он ранее не был зарегистрирован")
    def test_courier_login_not_found(self, create_new_courier_and_delete_after_test):
        data = create_new_courier_and_delete_after_test
        response = requests.post(COURIER_LOGIN, json={"login": data['login'], "password": data['password']})
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Тест проверяет, что если ввести верный логин и неверный пароль, авторизация не произойдет")
    def test_courier_login_invalid_password(self, create_new_courier_and_delete_after_test):
        data = create_new_courier_and_delete_after_test
        requests.post(COURIER, json=data)
        response = requests.post(COURIER_LOGIN, json={"login": data['login'], "password": 123})
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

