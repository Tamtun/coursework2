from src.api.hh_api import HeadHunterAPI
from src.models.vacancy import Vacancy
from src.storage.json_saver import JSONSaver


def user_interaction():
    """Функция для взаимодействия с пользователем."""
    hh_api = HeadHunterAPI()
    json_saver = JSONSaver()

    # Ввод поискового запроса
    search_query = input("Введите поисковый запрос: ")

    # Получение вакансий
    vacancies_data = hh_api.get_vacancies(search_query)

    # Преобразуем данные в объекты Vacancy
    vacancies = [
        Vacancy(
            v["name"],
            v["alternate_url"],
            v["salary"]["from"] if v["salary"] else "Зарплата не указана",
            v["snippet"]["requirement"],
        )
        for v in vacancies_data
    ]

    # Ввод количества вакансий для топа
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    # Ввод ключевых слов для фильтрации
    filter_words = input(
        "Введите ключевые слова для фильтрации вакансий (через пробел): "
    ).split()

    # Фильтрация вакансий по ключевым словам
    filtered_vacancies = [
        v
        for v in vacancies
        if any(word.lower() in v.description.lower() for word in filter_words)
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
