import pytest
from unittest.mock import patch
from src.api.hh_api import HHAPI


@pytest.fixture
def hh_api():
    """Фикстура для работы с HHAPI."""
    return HHAPI()


@patch("requests.get")
def test_get_vacancies(mock_get, hh_api):
    """Тест получения вакансий с мокированным API hh.ru."""

    # Фейковый ответ API
    mock_response = {
        "items": [
            {
                "name": "Python Developer",
                "alternate_url": "https://hh.ru/vacancy/123",
                "salary": {"from": 100000},
                "snippet": {"requirement": "Опыт работы 3 года"},
            },
            {
                "name": "Data Scientist",
                "alternate_url": "https://hh.ru/vacancy/456",
                "salary": {"from": 120000},
                "snippet": {"requirement": "Опыт работы 2 года"},
            },
        ]
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    vacancies = hh_api.get_vacancies("Python")

    assert len(vacancies) == 2
    assert vacancies[0]["name"] == "Python Developer"
    assert vacancies[1]["name"] == "Data Scientist"
