import requests

from project_4_3.config.constant import BASE_URL, API_HEADERS
import random

class TestItems():
    # POST /items — создание нового элемента.
    endpoint = f"{BASE_URL}/api/v1/items/"

    def test_create_items(self, auth_session, item_data):
        responce_item = auth_session.post(self.endpoint, json=item_data)
        assert responce_item.status_code in (200, 201), f"Responce: {responce_item.status_code}, {responce_item.text}"

        data = responce_item.json()
        item_id = data.get("id")
        assert item_id is not None
        assert data.get("title") == item_data["title"]
        # assert data.get["description"] == item_data["description"], "Описание не совпадает"

        """Создание нового атрибута в классе, где будет значение id созданного объекта"""
        self.created_item_id = item_id

    def test_create_items_not_auth(self, item_data):
        responce = requests.post(self.endpoint, json=item_data)
        assert responce.status_code == 401, f"Статус код: {responce.status_code} без авторизации"

    def test_create_not_valid_data(self, auth_session, item_data_not_valid):
        responce = auth_session.post(self.endpoint, json=item_data_not_valid)
        assert responce.status_code == 422, f"Стутус код: {responce.status_code}, {responce.text}"

    def test_create_not_valid_data_2(self, auth_session, item_data_not_valid_2):
        responce = auth_session.post(self.endpoint, json=item_data_not_valid_2)
        assert responce.status_code == 422, f"Стутус код: {responce.status_code}, {responce.text}"


    # GET /api/v1/items/
    def test_get_items(self, auth_session):
        responce = auth_session.get(self.endpoint)
        assert responce.status_code == 200, f"Responce: {responce.status_code}, {responce.text}"

        if responce.status_code == 200:
            items = responce.json()
            print("\n Список при получении элементов:", items)
        else:
            print("\n Ошибка при получении элементов, статус код:", responce.status_code)

        data = responce.json()
        assert "data" in data, "Responce missing 'data' key"
        assert isinstance(data["data"], list), "'data' is not a list"
        assert "count" in data, "Responce missing 'count' key"
        assert isinstance(data["count"], int), "'count' should be integer"

        assert data["count"] == len(data["data"]), "'count' должно соотвествовать количеству элементов в 'data'"

        # Проверяем каждый элемент в списке
        for item in data["data"]:
            assert "title" in item, "Отсутствует ключ 'title' в массиве"
            assert "description" in item, "Отсутствует ключ 'description' в массиве"
            assert "id" in item, "Отсутствует ключ 'id' в массиве"
            assert "owner_id" in item, "Отсутствует ключ 'owner_id' в массиве"

            assert isinstance(item["title"], str), "Поле 'title' должно быть строкой"
            assert isinstance(item["description"], str), "Поле 'description' должно быть строкой"
            assert isinstance(item["id"], str), "Поле 'id' должно быть строкой"
            assert isinstance(item["owner_id"], str), "The 'owner_id' field must be of type str"

            # Проверка на непустоту идентификаторов
            assert len(item["id"]) > 0, "'id' не может быть пустым"
            assert len(item["owner_id"]) > 0, "'owner_id' не может быть пустым"

        # Фильтрация, сортировка и пагинация

    def test_get_items_query_params_1(self, auth_session):
        skip = 1
        responce = auth_session.get(f"{self.endpoint}?skip={skip}")

        if responce.status_code == 200:
            items = responce.json()
            print("\n Список элементов:", items)
        else:
            print("\n Ошибка при получении элементов, статус код: ", responce.status_code)

        data = responce.json()
        assert "data" in data, "Responce missing 'data' key"
        assert isinstance(data["data"], list), "'data' is not a list"
        assert "count" in data, "Responce missing 'count' key"
        assert isinstance(data["count"], int), "'count' should be integer"

        assert data["count"] - 1 == len(data["data"]), "'count' - 1 должен быть равен кол-ву элементов в списке"


    def test_get_items_query_params_2(self, auth_session):
        limit = random.randint(1, 10)
        responce = auth_session.get(f"{self.endpoint}?limit={limit}")

        if responce.status_code == 200:
            items = responce.json()
            print(f"\n Список элементов с лимитом {limit}:", items)
        else:
            print("\n Ошибка при получении списка элементов, статус код:", responce.status_code)

        data = responce.json()
        assert "data" in data, "Responce missing 'data' key"
        assert isinstance(data["data"], list), "'data' is not a list"
        assert "count" in data, "Responce missing 'count' key"
        assert isinstance(data["count"], int), "'count' should be integer"

        assert limit == len(data["data"]), "Кол-во элементов не совпадает в лимитом"

    def test_get_items_query_params_3(self, auth_session):
        skip = 5
        limit = random.randint(11, 20)
        params = {"skip": {skip}, "limit": {limit}}
        responce = auth_session.get(f"{self.endpoint}", params=params)

        if responce.status_code == 200:
            items = responce.json()
            print(f"\n Список элементов с параметрами skip={skip}, limit={limit}: ", items)
        else:
            print(f"\n Ошибка при получении списка элементов с параметрами skip={skip}, limit={limit}: ",
                  responce.status_code, responce.text)

        data = responce.json()
        assert "data" in data, "Responce missing 'data' key"
        assert isinstance(data["data"], list), "'data' is not a list"
        assert "count" in data, "Responce missing 'count' key"
        assert isinstance(data["count"], int), "'count' should be integer"

        # assert data["count"] - 1 == len(data["data"]), "'count' - 1 должен быть равен кол-ву элементов в списке"
        assert limit == len(data["data"]), "Кол-во элементов не совпадает в лимитом"

    def test_get_items_not_auth(self):
        skip = 5
        limit = random.randint(11, 20)
        params = {"skip": {skip}, "limit": {limit}}

        # В постмане статус код 401, через pyCharm 404
        responce = requests.get(f"{self.endpoint}", params=params, headers=API_HEADERS)
        assert responce.status_code == 401, f"Статус код: {responce.status_code} без авторизации"

    # def test_query_params_not_valid(self, auth_session):
    #     responce = auth_session.get(self.endpoint}?")

    def test_filter_by_id(self, auth_session):
        """Предполагается, что API поддерживает фильтрацию через параметры запроса"""

        id_filter = "00b75c96-355d-4272-8b68-79c3409a1c80"
        responce = auth_session.get(f"{self.endpoint}{id_filter}")

        # assert responce.status_code == 200, f"Нет данных по id: {responce.status_code}, {responce.text}"
        if responce.status_code == 200:
            item = responce.json()
            print(f"\n Данные по id {id_filter}: {item}")
        else:
            print(f"Ошибка при фильтрации по id: {responce.status_code}, {responce.text}")

        id_filter_2 = "0"
        responce_2 = auth_session.get(f"{self.endpoint}{id_filter_2}")

        # assert responce.status_code == 200, f"Нет данных по id: {responce.status_code}, {responce.text}"
        if responce_2.status_code == 200:
            item_2 = responce_2.json()
            print("\n Данные по id: ", item_2)
        else:
            print(f"Нет данных по id: {responce_2.status_code}, {responce_2.text}")

    def test_filter_by_title(self, auth_session):
        title_filter = "worry"
        responce = auth_session.get(f"{self.endpoint}{title_filter}")

        if responce.status_code == 200:
            # return f"\n Данные по title: {responce.json()}"
            item = responce.json()
            print("\n Данные по title: ", item)
        else:
            print(f"Ошибка при фильтрации по title: {responce.status_code}, {responce.text}")


        title_filter_2 = "w"
        responce_2 = auth_session.get(f"{self.endpoint}{title_filter_2}")

        if responce_2.status_code == 200:
            item_2 = responce_2.json()
            print("\n Данные по title: ", item_2)
        else:
            print(f"\n Нет данных по title: {responce_2.status_code}, {responce_2.text}")

    def test_filter_by_description(self, auth_session):
        description_filter = "Indeed reason wonder wall pass increase part stand name doctor soldier role."
        responce = auth_session.get(f"{self.endpoint}{description_filter}")

        if responce.status_code == 200:
            item = responce.json()
            print("\n Данные по title: ", item)
        else:
            print(f"\n Нет данных по title: {responce.status_code}, {responce.text}")

    def test_filter_by_owner_id(self, auth_session):
        owner_id_filter = "9ec80f1e-12e2-488d-a6f3-96db4aca8149"
        responce = auth_session.get(f"{self.endpoint}{owner_id_filter}")

        if responce.status_code == 200:
            item = responce.json()
            print("\n Данные по title: ", item)
        else:
            print(f"\n Нет данных по title: {responce.status_code}, {responce.text}")

    def test_sort_by_title(self, auth_session):


    # PUT /items/{id} — полное обновление элемента.
    def test_update_item(self, auth_session, item_data, item_data_update):
        post_responce = auth_session.post(f"{self.endpoint}", json=item_data)
        assert post_responce.status_code == 200, (f"Неверный статус код при создании объекта: "
                                                  f"{post_responce.status_code}, тело ответа: {post_responce.text}")

        item_id = post_responce.json().get("id")
        put_responce = auth_session.put(f"{self.endpoint}{item_id}", json=item_data_update)
