STATUS_OK = {"ok": True}
CREATE_COURIER_BAD_REQUEST = "Недостаточно данных для создания учетной записи"
CREATE_COURIER_ALREADY_EXISTS = "Этот логин уже используется. Попробуйте другой."

COURIER_LOGIN_BAD_REQUEST = "Недостаточно данных для входа"
COURIER_LOGIN_NOT_FOUND = "Учетная запись не найдена"

DELETE_COURIER_NOT_FOUND = "Not Found"
DELETE_COURIER_NOT_FOUND_BY_ID = "Курьера с таким id нет."

MAIN_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

COURIER = f"{MAIN_URL}/courier"
COURIER_LOGIN = f"{MAIN_URL}/courier/login"
ORDER_URL = f"{MAIN_URL}/orders"

ORDER_DATA = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha"
}
