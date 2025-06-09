class Vacancy:
    """Класс для представления вакансии."""

    __slots__ = ("title", "link", "salary", "description")

    def __init__(self, title: str, link: str, salary: str, description: str):
        self.title = title
        self.link = link
        self.salary = self._validate_salary(salary)
        self.description = description

    def _validate_salary(self, salary):
        """Проверка зарплаты: если не указана, устанавливаем 'Зарплата не указана'."""
        return salary if salary else "Зарплата не указана"

    def _convert_salary(self):
        """Преобразует зарплату в числовой формат для сравнения."""
        if isinstance(self.salary, int):
            return self.salary
        if self.salary == "Зарплата не указана":
            return 0
        try:
            return int(self.salary.split("-")[0].replace(" ", "").strip())
        except ValueError:
            return 0

    def __gt__(self, other):
        """Сравнение вакансий по зарплате (большее значение)."""
        return self._convert_salary() > other._convert_salary()

    def __lt__(self, other):
        """Сравнение вакансий по зарплате (меньшее значение)."""
        return self._convert_salary() < other._convert_salary()

    def __eq__(self, other):
        """Сравнение вакансий по зарплате."""
        if not isinstance(other, Vacancy):
            return False
        return self._convert_salary() == other._convert_salary()

    def __repr__(self):
        return f"{self.title} ({self.salary}): {self.link}"
