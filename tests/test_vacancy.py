import pytest
from src.models.vacancy import Vacancy


def test_vacancy_init():
    """Проверка корректного создания объекта Vacancy."""
    vacancy = Vacancy(
        "Python Dev", "https://example.com", "120000", "Требуется опыт работы"
    )
    assert vacancy.title == "Python Dev"
    assert vacancy.link == "https://example.com"
    assert vacancy.salary == "120000"
    assert vacancy.description == "Требуется опыт работы"


def test_vacancy_comparison():
    """Проверка сравнения вакансий по зарплате."""
    v1 = Vacancy("Dev1", "https://example.com/1", "90000", "Тест")
    v2 = Vacancy("Dev2", "https://example.com/2", "120000", "Тест")
    assert v2 > v1


def test_convert_salary():
    """Проверка метода `_convert_salary()`."""
    v1 = Vacancy("Dev1", "https://example.com/1", "90000", "Тест")
    v2 = Vacancy("Dev2", "https://example.com/2", "120 000 - 150 000", "Тест")
    v3 = Vacancy("Dev3", "https://example.com/3", None, "Тест")

    assert v1._convert_salary() == 90000
    assert v2._convert_salary() == 120000
    assert v3._convert_salary() == 0


def test_repr():
    """Проверка метода `__repr__()`."""
    vacancy = Vacancy("Python Dev", "https://example.com", "120000", "Опыт работы")
    assert repr(vacancy) == "Python Dev (120000): https://example.com"


def test_equality():
    """Проверка сравнения вакансий (`__eq__()` и `__lt__()`)."""
    v1 = Vacancy("Dev1", "https://example.com/1", "90000", "Тест")
    v2 = Vacancy("Dev2", "https://example.com/2", "90000", "Тест")
    v3 = Vacancy("Dev3", "https://example.com/3", None, "Тест")

    assert v1 == v2
    assert v3 < v1


if __name__ == "__main__":
    pytest.main()
