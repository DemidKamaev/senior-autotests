from requests_lesson_4_1.constant import BASE_URL

class TestGetBooking():
    # GET апи общая
    # 1 Тест. Общие тесты без указания конкретного ID
    def test_valid_url(self, auth_session):
        get_booking = auth_session.get(f"{BASE_URL}")
        assert get_booking.status_code == 200, "Ошибка при запросе данных"

        # try:
        #     get_bookings = get_booking.json()
        # except ValueError as e:
        #     assert False, f"Ошибка разрабора JSON: {str(e)}"

        # Скорее всего здесь переменной get_bookings не хватает памяти(нужен пагинация)

        # Инициализируем список для хранения всех бронирований
        all_bookings = []

        # Начальные значения для пагинации
        page = 1
        limit = 30

        while True:
            # Формируем url с параметрами для пагинации
            get_booking = auth_session.get(f"{BASE_URL}?page={page}&limit={limit}")
            assert get_booking.status_code == 200, "Ошибка при запросе ограниченных данных"

            # Преобразуем ответ в список
            # ********На данной строке падает тест*******
            get_bookings = get_booking.json()   # Преполагаем, что здесь возвращается список

            # Если возвращаемое значение пустое, выходим из цикла
            if not get_bookings:
                break

            # Добавляем полученнные бронирования к общему списоку
            all_bookings.extend(get_bookings)

            # Переход к след странице
            # page += 1

        # Проверка типа переменной get_bookings
        assert isinstance(get_bookings, list), "Ответ запроса не является списком"
        assert len(all_bookings) > 0, "Не найдено ни одной записи бронирования"
        assert any("bookingid" in i for i in all_bookings)


    # GET апи с квери параметрами
    def test_get_bookings_with_query(self, auth_session, booking_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Бронь не создана/проверить доку"

        get_responce = auth_session.get(f"{BASE_URL}/booking?"
                                        f"firstname={booking_data['firstname']}"
                                        f"&lastname={booking_data['lastname']}")
                                        # f"&checkin={booking_data['bookingdates']['checkin']}"
                                        # f"&checkout={booking_data['bookingdates']['checkout']}")
        assert get_responce.status_code == 200, "Статус ответа на запрос по корнкретным данным: имени и фамилли не 200"
        """метод json возвращает словарь, но при вызове гета ответ является списком
        Если ответ является списком, то нет необходимости использовать .get().
        Вместо этого мы можете работать с данным списком напрямую."""

        # преобразование ответа в JSON
        bookings = get_responce.json()

        # Проверка, что список бронирований не пустой
        assert len(bookings) > 0, "Список бронирования с сортировкой по имени пуст"

        # Извлечение id
        booking_id = bookings[0]["bookingid"]
        assert booking_id is not None, "Booking ID не найден в списке"


# Чтобы тест не падал использовать пагинацию для большого объема данных
# Для переменной get_bookings использовать цикл, который будет отправлять повторяющиеся HTTP-запросы к API,
# изменяя параметры URL, чтобы получать разные страницы результатов.
# Обычно API предоставляет информацию о пагинации,
# такую как номер текущей страницы и количество элементов на странице.
