import json
from src.storage.abstract_storage import AbstractStorage
from src.models.vacancy import Vacancy  # Импортируем класс Vacancy

class JsonSaver(AbstractStorage):
    """Класс для работы с JSON-файлами."""

    def __init__(self, filename="vacancies.json"):
        self._filename = filename  # Сделали имя файла приватным

    def get_data(self):
        """Получение данных из файла."""
        try:
            with open(self._filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def add_data(self, data):
        """Добавление данных в файл без перезаписи."""
        existing_data = self.get_data()
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump(existing_data + [data], file, indent=4)

    def delete_data(self):
        """Удаление данных (очистка файла)."""
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump([], file)

    def _load_vacancies(self):
        """Приватный метод загрузки вакансий из файла."""
        return self.get_data()

    def add_vacancy(self, vacancy: Vacancy):
        """Добавление вакансии в JSON-файл без перезаписи и без дублей."""
        vacancies = self._load_vacancies()

        # Проверяем, нет ли уже такой вакансии (по ссылке)
        if not any(v["link"] == vacancy.link for v in vacancies):
            vacancies.append({
                "title": vacancy.title,
                "link": vacancy.link,
                "salary": vacancy.salary,
                "description": vacancy.description,
            })

        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4)

    def delete_vacancy(self, vacancy: Vacancy):
        """Удаление вакансии из JSON-файла по ссылке."""
        vacancies = self._load_vacancies()
        vacancies = [v for v in vacancies if v["link"] != vacancy.link]

        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, indent=4)
