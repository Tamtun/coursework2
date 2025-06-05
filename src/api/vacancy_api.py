from abc import ABC, abstractmethod


class VacancyAPI(ABC):
    """Абстрактный класс для работы с API платформ с вакансиями."""

    @abstractmethod
    def get_vacancies(self, query: str):
        """Получает вакансии по заданному запросу."""
        pass
