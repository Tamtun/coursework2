from src.api.hh_api import HHAPI  # Исправлен импорт
from src.models.vacancy import Vacancy
from src.storage.json_saver import JsonSaver  # Исправлен импорт

def user_interaction():
    """Функция для взаимодействия с пользователем."""
    hh_api = HHAPI()  # Исправлено название класса
    json_saver = JsonSaver()

    try:
        # Ввод поискового запроса
        search_query = input("Введите поисковый запрос: ")
        vacancies_data = hh_api.get_vacancies(search_query)

        # Преобразуем данные в объекты Vacancy
        vacancies = [
            Vacancy(
                v["name"],
                v["alternate_url"],
                v["salary"]["from"] if v.get("salary") and v["salary"].get("from") else "Зарплата не указана",
                v["snippet"]["requirement"] if v.get("snippet") and v["snippet"].get("requirement") else "Нет требований",
            )
            for v in vacancies_data
        ]
    except Exception as e:
        print(f"Ошибка при получении вакансий: {e}")
        return

    # Ввод количества вакансий для топа
    try:
        top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    except ValueError:
        print("Ошибка: Введите числовое значение.")
        return

    # Ввод ключевых слов для фильтрации
    filter_words = input(
        "Введите ключевые слова для фильтрации вакансий (через пробел): "
    ).split()

    # Фильтрация вакансий по ключевым словам
    filtered_vacancies = [
        v
        for v in vacancies
        if any(word.lower() in (v.description or "").lower() for word in filter_words)
    ]

    # Сортировка по зарплате
    sorted_vacancies = sorted(filtered_vacancies, reverse=True)

    # Вывод топ N вакансий
    print("\nТоп вакансий:")
    for vacancy in sorted_vacancies[:top_n]:
        print(vacancy)

    # Сохранение вакансий
    for vacancy in sorted_vacancies[:top_n]:
        json_saver.add_vacancy(vacancy)

    print("\nВакансии успешно сохранены!")

if __name__ == "__main__":
    user_interaction()
