from abc import ABC, abstractmethod
import doctest
from book import Book


class Library(ABC):
    """
    Абстрактный класс, описывающий библиотеку.
    """

    def __init__(self, name: str, capacity: int):
        """
        Инициализация библиотеки.

        :param name: Название библиотеки
        :param capacity: Максимальное количество книг

        Примеры:
        >>> class TestBook(Book):
        ...     def read(self, pages: int) -> int:
        ...         return pages
        ...     def get_pages_count(self) -> int:
        ...         return 100
        >>> class TestLibrary(Library):
        ...     def add_book(self, book: Book) -> None:
        ...         if len(self.books) >= self.capacity:
        ...             raise ValueError("Библиотека переполнена")
        ...         self.books.append(book)
        ...     def remove_book(self, title: str) -> bool:
        ...         for b in self.books:
        ...             if b.title == title:
        ...                 self.books.remove(b)
        ...                 return True
        ...         return False
        >>> library = TestLibrary("City Library", 10)
        >>> library.name
        'City Library'
        >>> library.capacity
        10
        >>> len(library.books)
        0
        """
        if not isinstance(name, str):
            raise TypeError("Название библиотеки должно быть строкой")
        if not name:
            raise ValueError("Название библиотеки не может быть пустым")

        if not isinstance(capacity, int):
            raise TypeError("Вместимость должна быть целым числом")
        if capacity <= 0:
            raise ValueError("Вместимость должна быть положительным числом")

        self.name: str = name
        self.capacity: int = capacity
        self.books: list[Book] = []

    @abstractmethod
    def add_book(self, book: Book) -> None:
        """
        Добавить книгу в библиотеку.

        :param book: Экземпляр книги
        :return: None

        Примеры:
        >>> class TestBook(Book):
        ...     def read(self, pages: int) -> int:
        ...         return pages
        ...     def get_pages_count(self) -> int:
        ...         return 100
        >>> class TestLibrary(Library):
        ...     def add_book(self, book: Book) -> None:
        ...         if len(self.books) >= self.capacity:
        ...             raise ValueError("Библиотека переполнена")
        ...         self.books.append(book)
        ...     def remove_book(self, title: str) -> bool:
        ...         return False
        >>> library = TestLibrary("City Library", 1)
        >>> library.add_book(TestBook("Python", 100))
        >>> len(library.books)
        1
        """
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        """
        Удалить книгу из библиотеки по названию.

        :param title: Название книги
        :return: Удалена ли книга

        Примеры:
        >>> class TestBook(Book):
        ...     def read(self, pages: int) -> int:
        ...         return pages
        ...     def get_pages_count(self) -> int:
        ...         return 100
        >>> class TestLibrary(Library):
        ...     def add_book(self, book: Book) -> None:
        ...         self.books.append(book)
        ...     def remove_book(self, title: str) -> bool:
        ...         for b in self.books:
        ...             if b.title == title:
        ...                 self.books.remove(b)
        ...                 return True
        ...         return False
        >>> library = TestLibrary("City Library", 5)
        >>> library.add_book(TestBook("Python", 100))
        >>> library.remove_book("Python")
        True
        """
        pass


if __name__ == "__main__":
    doctest.testmod()