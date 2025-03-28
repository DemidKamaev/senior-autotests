from requests_lesson_4_1.constant import BASE_URL

class TestGetBooking():
    # 1 Тест
    def test_valid_url(self, auth_session):
        get_booking = auth_session.get(f"{BASE_URL}")
        assert get_booking.status_code == 200, "Ошибка при запросе данных"

    # 2 тест. Тест падает даже с обработчиком исключения
    def test_params_url(self, auth_session):
        get_booking_2 = auth_session.get(f"{BASE_URL}?firstname=sally&lastname=brown")
        assert get_booking_2.status_code == 200, "Ошибка при запросе данных"
        print(get_booking_2.text)  # Для отладки

        # Преобразуем ответ в JSON
        try:
            get_responce = get_booking_2.json()  # Используем .json() для преобразования в dict
        except ValueError as e:
            assert False, f"Ошибка разрабора JSON: {str(e)}"

        # Проверяем, что имя и фамилия совпадают
        assert get_responce["firstname"] == "sally", "Имя другое/Нет данных"
        assert get_responce["lastname"] == "brown", "Фамилия другая/Нет данных"


