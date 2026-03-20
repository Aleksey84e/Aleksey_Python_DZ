import pytest
import uuid
from api_client import ProjectAPI

BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = "" # Вставить ключ

@pytest.fixture
def api():
    return ProjectAPI(BASE_URL, TOKEN)

@pytest.fixture
def temp_project(api):
    """Фикстура для создания и автоматического удаления проекта"""
    title = f"Test Project {uuid.uuid4()}"
    response = api.create_project(title)
    project_id = response.json().get("id")
    yield project_id
    # Очистка после теста
    if project_id:
        api.delete_project(project_id)

# --- ПОЗИТИВНЫЕ ТЕСТЫ ---

def test_create_project_positive(api):
    title = f"New Project {uuid.uuid4()}"
    response = api.create_project(title)
    assert response.status_code == 201
    assert response.json()["title"] == title
    # Удаляем за собой
    api.delete_project(response.json()["id"])

def test_get_project_positive(api, temp_project):
    response = api.get_project(temp_project)
    assert response.status_code == 200
    assert response.json()["id"] == temp_project

def test_update_project_positive(api, temp_project):
    new_title = "Updated Title"
    response = api.update_project(temp_project, new_title)
    assert response.status_code == 200
    assert response.json()["title"] == new_title

# --- НЕГАТИВНЫЕ ТЕСТЫ ---

def test_create_project_empty_title(api):
    # Попытка создания без обязательного поля title
    response = api.create_project("")
    assert response.status_code == 400

def test_get_non_existent_project(api):
    # Попытка получить проект с несуществующим ID
    fake_id = str(uuid.uuid4())
    response = api.get_project(fake_id)
    assert response.status_code == 404

def test_update_project_invalid_id(api):
    # Попытка обновить проект с некорректным ID
    response = api.update_project("invalid-id-123", "New Title")
    assert response.status_code in [400, 404]
