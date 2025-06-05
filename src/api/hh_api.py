import requests
from src.api.vacancy_api import VacancyAPI


class HeadHunterAPI(VacancyAPI):
    """Класс для получения вакансий с платформы hh.ru."""

    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, query: str):
        """Получает список вакансий с hh.ru по запросу."""
        params = {"text": query, "per_page": 20}  # Можно изменить количество вакансий
        response = requests.get(self.BASE_URL, params=params)

        if response.status_code == 200:
            return response.json()["items"]
        else:
            print(f"Ошибка: {response.status_code}")
            return []
