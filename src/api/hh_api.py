import requests
from src.api.abstract_api import AbstractAPI

class HHAPI(AbstractAPI):
    """Класс для работы с API hh.ru."""

    def __init__(self):
        self._base_url = "https://api.hh.ru/vacancies"

    def _connect(self):
        """Приватный метод подключения к API hh.ru."""
        response = requests.get(self._base_url)
        if response.status_code != 200:
            raise Exception(f"Ошибка подключения: {response.status_code}")
        return response.json()

    def get_vacancies(self, keyword):
        """Получение вакансий по ключевому слову."""
        params = {"text": keyword, "per_page": 20}
        response = requests.get(self._base_url, params=params)
        if response.status_code != 200:
            raise Exception(f"Ошибка получения вакансий: {response.status_code}")
        return response.json().get("items", [])
