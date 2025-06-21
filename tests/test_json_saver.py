import pytest
import json
import os
from src.models.vacancy import Vacancy
from src.storage.json_saver import JsonSaver


@pytest.fixture
def json_saver():
    """Фикстура для тестирования JsonSaver (используем временный файл)."""
    return JsonSaver("tests/temp_vacancies.json")


@pytest.fixture(scope="function", autouse=True)
def cleanup_json_file():
    """Удаляет тестовый JSON-файл после каждого теста."""
    yield  # Даем тесту выполниться
    temp_file = "tests/temp_vacancies.json"
    if os.path.exists(temp_file):
        os.remove(temp_file)


def test_add_vacancy(json_saver):
    """Проверка добавления вакансии в JSON."""
    vacancy = Vacancy("Python Dev", "https://example.com", "120000", "Опыт работы")
    json_saver.add_vacancy(vacancy)

    vacancies = json_saver._load_vacancies()
    assert len(vacancies) > 0
    assert vacancies[0]["title"] == "Python Dev"


def test_delete_vacancy(json_saver):
    """Проверка удаления вакансии из JSON."""
    vacancy = Vacancy("Python Dev", "https://example.com", "120000", "Опыт работы")
    json_saver.add_vacancy(vacancy)
    json_saver.delete_vacancy(vacancy)

    vacancies = json_saver._load_vacancies()
    assert vacancy.link not in [v["link"] for v in vacancies]


def test_json_file_format(json_saver):
    """Проверка правильного формата JSON."""
    vacancy = Vacancy("Python Dev", "https://example.com", "120000", "Опыт работы")
    json_saver.add_vacancy(vacancy)

    with open("tests/temp_vacancies.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    assert isinstance(data, list)
    assert len(data) > 0
