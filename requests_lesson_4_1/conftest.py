from unittest.mock import patch

import httpx
import pytest
import requests

from requests_lesson_4_1.constant import HEADERS, BASE_URL
from faker import Faker

faker = Faker()


# По сути экземпляр класса фейкер, у кот
# есть нам нужные методы

# Вынесем метод get_token и инициализацию сессии в отдельную фикстуру

@pytest.fixture(scope="session")
def auth_session():
    """Создаем сессию с авторизацией и возвращает объект"""
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_responce = session.post(f"{BASE_URL}/auth", json={"username": "admin", "password": "password123"})
    assert auth_responce.status_code == 200, "Ошибка авторизацииб статус код не 200"
    token = auth_responce.json().get("token")
    assert token is not None, "Токен не найдеен в ответе"

    session.headers.update({"Cookie": f"token={token}"})
    return session
    # То есть session будет обогащена нашим токеном, который мы получили
    # Плюс проверка, если его не будет, фикстура не запуститься и будет ошибка(ее обработка)

    # Декоратор @pytest.fixture(scope="session") определяет фикстуру,
    # которая будет создана один раз для всех тестов в сессии.

    # session = requests.Session() создает объект сессии requests,
    # который позволяет сохранять cookies и заголовки между запросами.

    # session.headers.update(HEADERS) Устанавливает необходимые заголовки
    # (например, Content-Type и Accept) для всех запросов в сессии.
    # Отправляет POST запрос на эндпоинт /auth для авторизации и
    # извлекает токен из ответа.

    # session.headers.update({"Cookie": f"token={token}"})
    # Добавляет токен авторизации в заголовки сессии, что позволяет
    # авторизовываться на сервере в последующих запросах.

    # return session Возвращает объект сессии, который затем используется
    # в тестах для выполнения запросов с авторизацией.


"""Вынесем booking_data в фикстуру, добавив рандомизацию данных, 
во избежания парадокса пестецида"""


@pytest.fixture()
def booking_data():  # Здесь скоуп нам не нужен, пусть он будет в виде функции,
    # чтобы для каждого теста нам сетапилось одинаковая дата
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-04-05",
            "checkout": "2025-04-08"
        },
        "additionalneeds": "Gym"
    }


# @pytest.fixture(): Определяет функцию как фикстуру pytest, которая
# может быть использована в тестах. Без указания scope, фикстура по умолчанию будет
# создаваться заново для каждого теста, где она используется.

# Возвращаемый объект: Функция возвращает словарь с данными для создания букинга.
# Эти данные включают имя, фамилию, общую стоимость, статус оплаты депозита,
# даты заезда и выезда, а также дополнительные потребности.

# fake.first_name(), fake.last_name(): Генерируют случайные имя и фамилию.
# fake.random_int(min=100, max=10000): Генерирует случайное число в заданном диапазоне,
# используемое как общая стоимость букинга.

# Фикстуры для пут запроса
# 1. Для валидного кейса
@pytest.fixture()
def booking_put_data():  # Здесь скоуп нам не нужен, пусть он будет в виде функции,
    # чтобы для каждого теста нам сетапилось одинаковая дата
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-04-05",
            "checkout": "2025-04-08"
        },
        "additionalneeds": "Gym"
    }


# 2. Для невалидного кейса без имени
@pytest.fixture()
def booking_put_data_2():  # Здесь скоуп нам не нужен, пусть он будет в виде функции,
    # чтобы для каждого теста нам сетапилось одинаковая дата
    return {
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-04-05",
            "checkout": "2025-04-08"
        },
        "additionalneeds": "Gym"
    }


# 3. Для проверки недопустимых значений
# Замена строки на инт "additionalneeds": 1000
@pytest.fixture()
def booking_put_data_3():  # Здесь скоуп нам не нужен, пусть он будет в виде функции,
    # чтобы для каждого теста нам сетапилось одинаковая дата
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-04-05",
            "checkout": "2025-04-08"
        },
        "additionalneeds": 1000
    }


# 4. Отправить json
@pytest.fixture()
def booking_put_data_4():  # Здесь скоуп нам не нужен, пусть он будет в виде функции,
    # чтобы для каждого теста нам сетапилось одинаковая дата
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
        },
        "additionalneeds": "Gym"
    }


# Функция - сделать запрос на исправление для проверки урла
# def make_put_request(url, data):
#     response = httpx.patch(url, json=data)
#     return response

# 5. как вызывать метод в фикструре, который как раз-таки вызывается
@patch('httpx.patch')
def test_put_request_sends_to_correct_url(mock_put, booking_put_data):
    url = BASE_URL
    data = booking_put_data

    make_put_request(url, data)

    # Проверьте, что patch вызван с правильным URL
    mock_put.assert_called_once_with(url, json=data)


# Фикстура для патч запроса, 1 тест
@pytest.fixture()
def booking_patch_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name()
    }


# 2 тест, невалиднные данные
@pytest.fixture()
def booking_patch_data_2():
    return {
        "firstname": 10,
        "lastname": faker.last_name()
    }

# 4 тест, 3 строки в теле-запроса
@pytest.fixture()
def booking_patch_data_4():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=10000)
    }