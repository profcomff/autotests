import pytest
import requests
from static.settings import get_settings

settings = get_settings()
BASE_URL = settings.BASE_TEST_STAND_URL  

class TestGetCommentByUUID:
    @pytest.fixture(scope="class")
    def create_lecturer_and_comment(self):

        # Создание преподавателя
        lecturer_url = f"{BASE_URL}/lecturer"
        lecturer_data = {
            "name": "Иван Иванов",
            "email": "ivan@example.com"
        }
        lecturer_response = requests.post(lecturer_url, json=lecturer_data)
        assert lecturer_response.status_code == 201, "Не удалось создать преподавателя"

        lecturer_id = lecturer_response.json()["id"]

        # Создание отзыва
        comment_url = f"{BASE_URL}/comment"
        comment_data = {
            "lecturer_id": lecturer_id,
            "text": "Отличный лектор!",
            "rating": 5
        }
        comment_response = requests.post(comment_url, json=comment_data)
        assert comment_response.status_code == 201, "Не удалось создать отзыв"

        comment_uuid = comment_response.json()["uuid"]

        # Возвращаем uuid отзыва для последующих проверок
        return comment_uuid
    def test_successful_get_comment(self, create_lecturer_and_comment):
        """
        Успешное получение отзыва по его uuid.
        Ожидается: статус 200 и все поля совпадают с отправленными.
        """

        comment_uuid = create_lecturer_and_comment
        url = f"{BASE_URL}/comment/{comment_uuid}"
        response = requests.get(url)

        # Проверяем статус-код
        assert response.status_code == 200, f"Ожидался статус-код 200, получено {response.status_code}"

        data = response.json()

        # Проверяем наличие ключевых полей
        expected_fields = ["uuid", "text", "rating", "lecturer_id"]
        for field in expected_fields:
            assert field in data, f"Поле '{field}' отсутствует в ответе"

        # Проверяем значения полей
        assert data["uuid"] == comment_uuid
        assert data["text"] == "Отличный лектор!"
        assert data["rating"] == 5

    def test_nonexistent_uuid(self):
        url = f"{BASE_URL}/comment/non-existent-uuid"
        response = requests.get(url)
        # Проверяем статус-код
        assert response.status_code == 404, f"Ожидался статус-код 404, получено {response.status_code}"

    def test_invalid_uuid_format():
        """
        Сценарий: Запрос с невалидным форматом UUID
        Ожидается: статус 422 Unprocessable Entity
        """
        url = f"{BASE_URL}/comment/123"  # Пример невалидного UUID
        response = requests.get(url)

        # Проверяем статус-код
        assert response.status_code == 422, f"Ожидался статус-код 422, получено {response.status_code}"

    def test_public_endpoint(self):
        url = f"{BASE_URL}/comment/some-uuid"
        response = requests.get(url)
        # Статусы: 200 - успех  или 404 ошибка
        assert response.status_code in [200, 404], \
            f"Эндпоинт должен быть публичным, получено {response.status_code}"