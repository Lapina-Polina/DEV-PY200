class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        # Название и автор книги (изменять нельзя)
        self._name = name
        self._author = author

    @property
    def name(self):
        """Возвращает название книги."""
        return self._name

    @property
    def author(self):
        """Возвращает автора книги."""
        return self._author

    def __str__(self):
        """Строковое представление книги для пользователя."""
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """Техническое представление объекта книги."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        # Инициализация базовых атрибутов
        super().__init__(name, author)
        # Количество страниц книги
        self.pages = pages

    @property
    def pages(self):
        """Возвращает количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, value):
        """Устанавливает количество страниц с проверкой."""
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше нуля")
        self._pages = value


class AudioBook(Book):
    """Класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        # Инициализация базовых атрибутов
        super().__init__(name, author)
        # Продолжительность аудиокниги
        self.duration = duration

    @property
    def duration(self):
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value):
        """Устанавливает продолжительность с проверкой."""
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше нуля")
        self._duration = float(value)