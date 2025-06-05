import json
from src.models.vacancy import Vacancy


class JSONSaver:
    """Класс для сохранения и работы с вакансиями в JSON."""

    def __init__(self, filename="data/vacancies.json"):
        self.filename = filename

    def add_vacancy(self, vacancy: Vacancy):
        """Добавляет вакансию в JSON-файл."""
        vacancies = self._load_vacancies()
        vacancies.append(vars(vacancy))
        self._save_vacancies(vacancies)

    def delete_vacancy(self, vacancy: Vacancy):
        """Удаляет вакансию из JSON-файла по ссылке."""
        vacancies = self._load_vacancies()
        vacancies = [v for v in vacancies if v["link"] != vacancy.link]
        self._save_vacancies(vacancies)

    def _load_vacancies(self):
        """Загружает вакансии из JSON-файла."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_vacancies(self, vacancies):
        """Сохраняет вакансии в JSON-файл."""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)
