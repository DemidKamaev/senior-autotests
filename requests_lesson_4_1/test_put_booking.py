import httpx
import unittest
from constant import BASE_URL



class TestPutBooking(unittest.TestCase):

    def test_check_put_booking(self, booking_data, auth_session, booking_put_data):
        # 1. Проверка необходимых заголовков для авторизации
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при созднии букинга"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID брони не найдено в ответе"

        # 2. Создание брони + Проверка созданной брони
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"

        # PUT апи для изменения брони + покрытие тестами
        # Используем фикстуру для пут от пост
        put_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=booking_put_data)
        # 3. Убедитесь, что ваш PUT-запрос возвращает статус код 200 OK
        assert put_booking.status_code == 200, f"Ошибка при изменении или создании брони с ID {booking_id}"
        # 4. Проверка, что данные успешно обновлены в базе данных или в системе.
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"

        # 5. Проверить, что данные, отправленные в теле запроса, соответствуют ожидаемой структуре. Накидать ассерты
        # Можно ли проверить тип данных + обязательные поля, если они указаны в сваггере?
        bookind_put_responce = get_booking.json()
        assert bookind_put_responce.json()["firstname"] == booking_put_data["firstname"], "Имя не совпадает"
        assert bookind_put_responce.json()["lastname"] == booking_put_data["lastname"], "Фамилия не совпадает"
        assert bookind_put_responce.json()["totalprice"] == booking_put_data["totalprice"], "Стоимость не совпадает"
        assert bookind_put_responce.json()["depositpaid"] == booking_put_data[
            "depositpaid"], "Статус депозита не совпадает"
        assert bookind_put_responce.json()["bookingdates"]["checkin"] == booking_put_data["bookingdates"][
            "checkin"], "Дата заезда не совпадает"
        assert bookind_put_responce.json()["bookingdates"]['checkout'] == booking_put_data["bookingdates"][
            'checkout'], "Дата выезда не совпадает"
        assert bookind_put_responce.json()["additionalneeds"] == "Gym", "Доп потребности не совпаадют"

    # 6. Убедиться, что запрос отправляется на правильный URL. Вопрос с реализацией тут, конечно)
    # def make_put_request(self, auth_session, booking_put_data, booking_id, test_put_request_sends_to_correct_url):

    #     responce = httpx.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_put_data)
    #     return responce
    #
    #     @patch('httpx.patch')
    #     def test_send_to_correct_url(self, mock_patch):
    #         # Как инициализировать booking_id
    #         url = f"{BASE_URL}/booking/{booking_id}"
    #         data = booking_data
    #
    #         make_patch_request(url, data)
    #
    #         # Проверить, что patch вызван с правильным UR
    #         mock_patch.assert_called_once_with(url, json=data)

    # if __name__ == '__main__':
    #     unittest.main()

    # 7. Проверка PUT-запроса с отсутствующими полями и проверить,
    # что возвращается статус код 400 Bad Request
    def test_check_not_fields(self, auth_session, booking_data, booking_put_data_2):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_put_data)
        assert create_booking.status_code == 200, "Ошибка при созднии букинга"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID брони не найдено в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"

        put_booking_2 = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=booking_put_data_2)
        assert put_booking_2.status_code == 404, f"Внесены изменении в бронь с ID {booking_id}"
        # Проверка, что данные остаются те же, что при создании брони(вытянуть json)
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении брони с ID {booking_id}"

        check_delete_booking = auth_session.get(f"s{BASE_URL}/booking/{booking_id}")
        assert check_delete_booking.status_code == 404, f"Букинг с ID {booking_id}"

    # 8. Проверка какие ошибки возникают при отправке недопустимых значений (например, неправильный тип данных,
    # слишком длинные строки и т. д.).
    def test_check_unaccepts_value(self, auth_session, booking_data, booking_put_data_3):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_put_data)
        assert create_booking.status_code == 200, "Ошибка при созднии букинга"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID брони не найдено в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"

        put_booking_3 = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=booking_put_data_3)
        assert put_booking_3.status_code == 403, f"Внесены изменения в бронь с ID {booking_id}"
        assert put_booking_3.json() == "Forbidden", "Другая ошибка"

        # Проверка, что данные остаются те же, что при создании брони(вытянуть json)
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"
        # Как нам проверить весь json, что не было никаких изменений?

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении брони с ID {booking_id}"

        check_delete_booking = auth_session.get(f"s{BASE_URL}/booking/{booking_id}")
        assert check_delete_booking.status_code == 404, f"Букинг с ID {booking_id}"

    # 9. Отправить json без дат регистрации
    def test_check_not_data_json(self, auth_session, booking_data, booking_put_data_4):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_put_data)
        assert create_booking.status_code == 200, "Ошибка при созднии букинга"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID брони не найдено в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"

        put_booking_4 = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=booking_put_data_4)
        assert put_booking_4.status_code == 403, "Внесены изменения в бронь, либо другая ошибка"
        assert put_booking_4.json() == "Forbidden", "Другая ошибка"

        # Проверить, что ничего не поломали по созданной брони, данные приходят
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении брони с ID {booking_id}"

        check_delete_booking = auth_session.get(f"s{BASE_URL}/booking/{booking_id}")
        assert check_delete_booking.status_code == 404, f"Букинг с ID {booking_id}"

    # 10. Проверка на уязвимости, такие как SQL Injection
    def test_sql_injection(self, auth_session, booking_put_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_put_data)
        assert create_booking.status_code == 200, "Ошибка при созднии букинга"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID брони не найдено в ответе"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"

        url = BASE_URL
        # Попытка выполнить SQL Injection
        mal_payload = "' OR '1'='1"

        put_booking_sql = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=booking_put_data)
        # Ожидаем, что приложение не вернет статус 200, если есть уязвимость
        self.assertNotEquals(put_booking_sql.status_code != 200, "200")
        # Дополнительная проверка на содержание в ответе данных, которые указывают на успешный
        # QL-инъекционный вывод
        self.assertNotIn('SQL', put_booking_sql.text) # или любой другой индикатор

    if __name__ == '__main__':
        unittest.main()



















# 1
# - Убедитесь, что вы работаете с актуальной версией API.
# - Узнайте формат данных, необходимые для PUT-запроса (JSON, XML и т. д.)

# 2
# - Проверьте необходимые заголовки для аутентификации (Bearer token, API key и т. д.)
# и убедитесь, что они правильно указаны.
# - Попробуйте выполнить запрос с невалидными учетными данными и убедитесь,
# что вы получаете соответствующее сообщение об ошибке.
# - Проверьте доступ к ресурсам для различных ролей пользователей (например,
# пользователь с ограниченными правами не должен иметь доступ к обновлению данных).

# 3
# - Убедитесь, что запрос отправляется на правильный URL.
# - Проверьте, что данные, отправленные в теле запроса,
#  соответствуют ожидаемой структуре и типам данных.
# - Убедитесь, что все обязательные поля присутствуют в запросе.

# 4
# - Убедитесь, что ваш PUT-запрос возвращает статус код 200 OK или 204 No Content
# (в зависимости от спецификации API) при успешном обновлении данных.
# - Проверьте, что ответ содержит актуализированные данные на основе отправленных.
# - Проверьте, что данные успешно обновлены в базе данных или в системе.

# 5
# - Отправьте PUT-запрос с отсутствующими обязательными полями и проверьте,
# что возвращается статус код 400 Bad Request и соответствующее сообщение об ошибке.
# - Проверьте, какие ошибки возникают при отправке недопустимых значений (например, неправильный тип данных,
# слишком длинные строки и т. д.).
# - Если применимо, отправьте запрос с некорректным идентификатором ресурса и убедитесь, что получаете 404 Not Found.