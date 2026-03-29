import requests

class ProjectAPI:
    def __init__(self, base_url, token):
        self.url = f"{base_url}/projects"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create(self, title):
        """Создание проекта (POST)"""
        return requests.post(self.url, json={"title": title}, headers=self.headers)

    def update(self, project_id, title):
        """Обновление проекта (PUT)"""
        return requests.put(f"{self.url}/{project_id}", json={"title": title}, headers=self.headers)

    def get_by_id(self, project_id):
        """Получение данных проекта (GET)"""
        return requests.get(f"{self.url}/{project_id}", headers=self.headers)

    def delete(self, project_id):
        """Удаление проекта (для очистки данных в тестах)"""
        return requests.delete(f"{self.url}/{project_id}", headers=self.headers)
