from abc import ABC, abstractmethod
import doctest


class Book(ABC):
    """
    Абстрактный класс, описывающий книгу.
    """

    def __init__(self, title: str, pages: int):
        """
        Инициализация книги.

        :param title: Название книги
        :param pages: Общее количество страниц

        Примеры:
        >>> class TestBook(Book):
        ...     def read(self, pages: int) -> int:
        ...         return min(pages, self.pages)
        ...     def get_pages_count(self) -> int:
        ...         return self.pages
        >>> book = TestBook("Python", 300)
        >>> book.title
        'Python'
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if title == "":
            raise ValueError("Название книги не может быть пустым")

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")

        self.title: str = title
        self.pages: int = pages

    @abstractmethod
    def read(self, pages: int) -> int:
        """
        Прочитать указанное количество страниц.

        :param pages: Количество страниц для чтения
        :return: Количество реально прочитанных страниц

        Примеры:
        >>> class TestBook(Book):
        ...     def read(self, pages: int) -> int:
        ...         return min(pages, self.pages)
        ...     def get_pages_count(self) -> int:
        ...         return self.pages
        >>> book = TestBook("Python", 300)
        >>> book.read(50)
        50
        """
        pass

    @abstractmethod
    def get_pages_count(self) -> int:
        """
        Получить общее количество страниц книги.

        :return: Общее количество страниц

        Примеры:
        >>> class TestBook(Book):
        ...     def read(self, pages: int) -> int:
        ...         return pages
        ...     def get_pages_count(self) -> int:
        ...         return 300
        >>> book = TestBook("Python", 300)
        >>> book.get_pages_count()
        300
        """
        pass


if __name__ == "__main__":
    doctest.testmod()