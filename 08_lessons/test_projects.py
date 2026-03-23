import pytest
import uuid
from api_client import ProjectAPI

# Настройки подключения
BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = "573vzPAdsIih2hRc7RaYfgYFYQSIARnXHggr2Mt6Ph2x00CLkBo+VXNs2jOwZayS"


@pytest.fixture
def api():
    return ProjectAPI(BASE_URL, TOKEN)


@pytest.fixture
def created_project(api):
    """
    Фикстура для создания проекта перед тестом и его удаления после.
    Обеспечивает независимость и стабильность тестов.
    """
    title = f"Project_{uuid.uuid4().hex[:8]}"
    response = api.create(title)
    project_id = response.json().get("id")
    yield project_id
    # Очистка: удаляем проект после завершения теста
    if project_id:
        api.delete(project_id)


# --- ПОЗИТИВНЫЕ ТЕСТЫ ---

def test_create_project_success(api):
    """Проверка создания проекта с валидным названием"""
    title = f"New_{uuid.uuid4().hex[:8]}"
    response = api.create(title)

    assert response.status_code == 201, "Ожидался статус 201 (Created)"
    assert response.json()["title"] == title
    # Удаляем за собой
    api.delete(response.json()["id"])


def test_get_project_success(api, created_project):
    """Проверка получения данных существующего проекта"""
    response = api.get_by_id(created_project)

    assert response.status_code == 200, "Ожидался статус 200 (OK)"
    assert response.json()["id"] == created_project


def test_update_project_success(api, created_project):
    """Проверка обновления названия проекта"""
    new_title = "Updated Title"
    response = api.update(created_project, new_title)

    assert response.status_code == 200
    assert response.json()["title"] == new_title


# --- НЕГАТИВНЫЕ ТЕСТЫ ---

def test_create_project_no_title(api):
    """Попытка создания проекта с пустым названием (Негативный)"""
    response = api.create("")
    # API Yougile обычно возвращает 400 при ошибке валидации
    assert response.status_code == 400


def test_get_project_invalid_id(api):
    """Запрос несуществующего проекта (Негативный)"""
    fake_id = str(uuid.uuid4())
    response = api.get_by_id(fake_id)

    assert response.status_code == 404, "Ожидался 404 для несуществующего ID"


def test_update_project_wrong_id(api):
    """Попытка обновить проект с некорректным ID (Негативный)"""
    response = api.update("invalid-id-format", "New Title")

    assert response.status_code in [400, 404]
