from abc import ABC, abstractmethod
import doctest


class Reader(ABC):
    """
    Абстрактный класс, описывающий читателя.
    """

    def __init__(self, name: str, age: int):
        """
        Инициализация читателя.

        :param name: Имя читателя
        :param age: Возраст читателя

        Примеры:
        >>> class TestReader(Reader):
        ...     def read_book(self, book_title: str) -> str:
        ...         return f"{self.name} читает книгу {book_title}"
        ...     def get_name(self) -> str:
        ...         return self.name
        >>> reader = TestReader("Anna", 25)
        >>> reader.name
        'Anna'
        >>> reader.age
        25
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not name:
            raise ValueError("Имя не может быть пустым")

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if age <= 0:
            raise ValueError("Возраст должен быть положительным числом")

        self.name: str = name
        self.age: int = age

    @abstractmethod
    def read_book(self, book_title: str) -> str:
        """
        Прочитать книгу.

        :param book_title: Название книги
        :return: Сообщение о чтении

        Примеры:
        >>> class TestReader(Reader):
        ...     def read_book(self, book_title: str) -> str:
        ...         return f"{self.name} читает книгу {book_title}"
        ...     def get_name(self) -> str:
        ...         return self.name
        >>> reader = TestReader("Anna", 25)
        >>> reader.read_book("Python")
        'Anna читает книгу Python'
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """
        Получить имя читателя.

        :return: Имя читателя

        Примеры:
        >>> class TestReader(Reader):
        ...     def read_book(self, book_title: str) -> str:
        ...         return ""
        ...     def get_name(self) -> str:
        ...         return self.name
        >>> reader = TestReader("Anna", 25)
        >>> reader.get_name()
        'Anna'
        """
        pass


if __name__ == "__main__":
    doctest.testmod()