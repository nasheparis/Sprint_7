import allure
import requests

from Sprint_7.data import COURIER_LOGIN, ORDER_URL, COURIER


class TestGetOrdersList:
    @allure.title("Тест проверяет получение общего списка заказов")
    def test_get_orders_list(self):
        response = requests.get(ORDER_URL)
        assert response.status_code == 200 and 'orders' in response.json()

    @allure.title("Тест проверяет получение списка заказов определенного курьера")
    def test_get_all_orders_for_courier_by_id(self, create_new_courier_and_delete_after_test):
        data = create_new_courier_and_delete_after_test
        requests.post(COURIER, json=data)
        response_login = requests.post(COURIER_LOGIN, json={"login": data['login'], "password": data['password']})
        courier_id = response_login.json().get('id', None)
        response = requests.get(f'{ORDER_URL}?courierId={courier_id}')
        assert response.status_code == 200 and 'orders' in response.json()

    @allure.title("Тест проверяет получение списка заказов курьера на станциях 1 или 2")
    def test_get_orders_near_stations_for_courier(self, create_new_courier_and_delete_after_test):
        data = create_new_courier_and_delete_after_test
        requests.post(COURIER, json=data)
        response_login = requests.post(COURIER_LOGIN, json={"login": data['login'], "password": data['password']})
        courier_id = response_login.json().get('id', None)
        response = requests.get(f'{ORDER_URL}?courierId={courier_id}&nearestStation=["1", "2"]')
        assert response.status_code == 200 and 'orders' in response.json()

    @allure.title("Тест проверяет получение списка 10 доступных заказов")
    def test_get_ten_available_orders(self):
        response = requests.get(f'{ORDER_URL}?limit=10&page=0')
        assert response.status_code == 200 and len(response.json()['orders']) <= 10

    @allure.title("Тест проверяет получение списка 10 доступных заказов возле станции 110")
    def test_get_limited_orders_near_station(self):
        response = requests.get(f'{ORDER_URL}?limit=10&page=0&nearestStation=["110"]')
        assert response.status_code == 200 and len(response.json()['orders']) <= 10

    @allure.title("Тест проверяет получение списка несуществующего курьера")
    def test_get_orders_of_nonexistent_courier(self):
        response = requests.get(f'{ORDER_URL}/?courierId=0')
        assert response.status_code == 404 and response.json().get('message') == "Курьер с идентификатором 0 не найден"


