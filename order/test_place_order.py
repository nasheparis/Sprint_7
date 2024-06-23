import allure
import pytest
import requests

from Sprint_7.data import ORDER_URL


@pytest.mark.parametrize(
    "color, expected_code", [
        (["BLACK"], 201),
        (["GREY"], 201),
        (["BLACK", "GREY"], 201),
        ([], 201),
        (None, 201)
    ],
    ids=[
        'Black only',
        'Grey only',
        'Both colors',
        'Empty',
        'None'
    ]
)
@allure.title("Тест проверяет создание заказа с разными значениями поля 'color'")
def test_create_order(order_data, color, expected_code):
    order_data["color"] = color or order_data.get("color")
    response = requests.post(ORDER_URL, json=order_data)
    response_data = response.json()
    assert response.status_code == expected_code and "track" in response_data
