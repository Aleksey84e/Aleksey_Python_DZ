import requests

class ProjectAPI:
    def __init__(self, base_url, token):
        self.base_url = f"{base_url}/projects"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        payload = {"title": title}
        return requests.post(self.base_url, json=payload, headers=self.headers)

    def update_project(self, project_id, title):
        payload = {"title": title}
        return requests.put(f"{self.base_url}/{project_id}", json=payload, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{self.base_url}/{project_id}", headers=self.headers)

    def delete_project(self, project_id):
        # Вспомогательный метод для очистки данных после тестов
        return requests.delete(f"{self.base_url}/{project_id}", headers=self.headers)
