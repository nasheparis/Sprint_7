* test_create_courier_positive - Тест проверяет успешное создание курьера
* test_create_courier_missing_required_data - Тест проверяет, что нельзя создать курьера, не указав обязательные поля
* test_create_courier_missing_required_password - Тест проверяет, что нельзя создать курьера, не указав хотя бы одно
  обязательное поле
* test_create_courier_missing_optional_data - Тест проверяет, что поле 'firstName' не обязательно для создания курьера
* test_create_courier_duplicate_login - Тест проверяет, что нельзя создать два одинаковых курьера
* test_create_courier_empty_request_body - Тест проверяет, что нельзя создать курьера, отправив пустое поле запроса

* test_courier_login_positive - Тест проверяет успешный логин курьера
* test_courier_login_missing_required_fields - Тест проверяет, что курьер не может авторизоваться, не указав
  обязательные поля
* test_courier_login_not_found - Тест проверяет, что курьер не может авторизоваться, если он ранее не был
  зарегистрирован
* test_courier_login_invalid_password - Тест проверяет, что если ввести верный логин и неверный пароль, авторизация не
  произойдет

* test_delete_courier_positive - Тест проверяет успешное удаление курьера
* test_delete_courier_without_id - Тест проверяет, что нельзя удалить курьера без id
* test_delete_courier_id_do_not_exist - Тест проверяет, что нельзя удалить курьера с несуществующим id

* test_create_order - Тест проверяет создание заказа с разными значениями поля 'color'

* test_get_orders_list - Тест проверяет получение общего списка заказов
* test_get_all_orders_for_courier_by_id - Тест проверяет получение списка заказов определенного курьера
* test_get_orders_near_stations_for_courier - Тест проверяет получение списка заказов курьера на станциях 1 или 2
* test_get_ten_available_orders - Тест проверяет получение списка 10 доступных заказов
* test_get_limited_orders_near_station - Тест проверяет получение списка 10 доступных заказов возле станции 110
* test_get_orders_of_nonexistent_courier - Тест проверяет получение списка несуществующего курьера





    

