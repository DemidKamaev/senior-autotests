from requests_lesson_4_1.constant import BASE_URL


class TestPatchBooking():
    # 1 тест
    def test_check_patch_booking(self, auth_session, booking_patch_data, booking_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при созднии букинга"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID брони не найдено в ответе"

        # Метод PATCH + покрытие тестами
        patch_booking_1 = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_patch_data)
        assert patch_booking_1.status_code == 200, f"Ошибка при изменении данных брони с ID {booking_id}"
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"

        booking_patch_responce = get_booking.json()
        assert booking_patch_responce["firstname"] == booking_patch_data["firstname"], "Имя совпадает"
        assert booking_patch_responce["lastname"] == booking_patch_data[
            "lastname"], "Фамилия совпадает, данные не обновились"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении брони с ID {booking_id}"

        check_delete_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert check_delete_booking.status_code == 404, f"Букинг с ID {booking_id}"

    # 2 тест
    def test_check_not_valid_value(self, auth_session, booking_data, booking_patch_data_2):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при созднии букинга"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID брони не найдено в ответе"
    #
    #     # В данном кейсе при измении имени на число (неверный тип данных) данные в постмане не обновляются (403 ошибка)
    #     # Через pytest тест падает, так как приходит статус 200 вместо 403
        patch_booking_2 = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_patch_data_2)
        assert patch_booking_2.status_code == 403, f"Внесены изменения в бронь с ID {booking_id}"
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"

        booking_patch_responce = get_booking.json()
        assert booking_patch_responce["lastname"] != booking_patch_data_2["lastname"], "Фамилии совпадает"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении брони с ID {booking_id}"

        check_delete_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert check_delete_booking.status_code == 404, f"Букинг с ID {booking_id}"

    # 3. Невалидный урл. Корректный ли данный тест?
    def test_check_not_valid_url(self, auth_session, booking_data, booking_patch_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при созднии букинга"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID брони не найдено в ответе"

        patch_booking_3 = auth_session.patch(f"{"https://restful-booker.heroku.com"}/booking/{booking_id}", json=booking_patch_data)
        assert patch_booking_3.status_code == 404, "Другой статус код"
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"

        delete_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert delete_booking.status_code == 201, f"Ошибка при удалении брони с ID {booking_id}"

        check_delete_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert check_delete_booking.status_code == 404, f"Букинг с ID {booking_id}"

    # 4. Отправить json с дополнительной строкой
    def test_check_json_3lines(self, auth_session, booking_data, booking_patch_data_4):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при созднии букинга"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "ID брони не найдено в ответе"

        # <Response [200]> != 403, Данные брони с ID обновились 1199
        patch_booking_4 = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json=booking_patch_data_4)
        assert patch_booking_4 == 403, f"Обновились данные в брони с ID {booking_id}"
        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, f"Ошибка при получении брони с ID {booking_id}"

        booking_patch_responce = get_booking.json()
        assert booking_patch_responce["firstname"] == booking_data["firstname"], "Данные в БД обновились по брони"
        assert booking_patch_responce["lasyname"] == booking_data["lastname"], "Фамилия обновилась"
        assert booking_patch_responce["totalprice"] == booking_data["totalprice"], "Стоимость поменялась"




