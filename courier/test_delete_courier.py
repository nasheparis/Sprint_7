import allure
import requests

from Sprint_7.data import COURIER_LOGIN, COURIER, STATUS_OK, DELETE_COURIER_NOT_FOUND, DELETE_COURIER_NOT_FOUND_BY_ID


class TestDeleteCourier:
    @allure.title("Тест проверяет успешное удаление курьера")
    def test_delete_courier_positive(self, create_new_courier_and_delete_after_test):
        data = create_new_courier_and_delete_after_test
        requests.post(COURIER, json=data)
        response_login = requests.post(COURIER_LOGIN, json={"login": data['login'], "password": data['password']})
        courier_id = response_login.json().get('id', None)
        response_delete = requests.delete(f'{COURIER}/{courier_id}')
        assert response_delete.status_code == 200 and response_delete.json() == STATUS_OK

    @allure.title("Тест проверяет, что нельзя удалить курьера без id")
    def test_delete_courier_without_id(self):
        response_delete = requests.delete(f'{COURIER}')
        assert response_delete.status_code == 404 or response_delete.json()["message"] == DELETE_COURIER_NOT_FOUND

    @allure.title("Тест проверяет, что нельзя удалить курьера с несуществующим id")
    def test_delete_courier_id_do_not_exist(self):
        response_delete = requests.delete(f'{COURIER}/0')
        assert response_delete.status_code == 404 and response_delete.json()[
            "message"] == DELETE_COURIER_NOT_FOUND_BY_ID
