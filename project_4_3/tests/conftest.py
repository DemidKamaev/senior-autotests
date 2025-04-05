import pytest
import requests
from project_4_3.config.constant import AUTH_HEADERS, BASE_URL, AUTH_DATA
from faker import Faker

fake = Faker()

@pytest.fixture(scope="session")
def auth_session():
    """Создаем сессию с авторизацией и возвращает объект"""
    session = requests.Session()
    responce = session.post(f"{BASE_URL}/api/v1/login/access-token", data=AUTH_DATA, headers=AUTH_HEADERS)
    assert responce.status_code == 200, f"Auth failed: {responce.status_code}, {responce.text}"

    token = responce.json().get("access_token")
    assert token is not None, "Токен в ответе не найден"

    # Обновляем заголовки сессии
    # Для выполнения API-запросов каждому пользователю необходимо
    # получить свой персональный токен авторизации.
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session


@pytest.fixture()
def item_data():
    """Генерация данных для создания нового элемента"""
    return {
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=10)
        # "title": faker.word(),
        # "description": faker.text()
    }

@pytest.fixture()
def item_data_not_valid():
    """Генерация данных для создания нового элемента"""
    return {
        "title": "",
        "description": None
    }

@pytest.fixture()
def item_data_not_valid_2():
    """Генерация данных для создания нового элемента"""
    return {
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=100)
    }

# Для апи PUT /items/{id}
@pytest.fixture()
def item_data_update():
    """Генерация данных для создания нового элемента"""
    return {
        "title": fake.word().capitalize(),
        "description": fake.sentence(nb_words=3)
    }
