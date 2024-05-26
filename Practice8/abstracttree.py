from abc import ABC, abstractmethod
from collections.abc import Iterable
from Practice1.employee import Employee


class AbstractTreeBasic(ABC):
    """Абстрактний клас - шаблон класу з переліком необхідних до реалізації базових методів структур даних без самої їх
    реалізації"""

    @abstractmethod
    def __init__(self, *args: Iterable[Employee]):
        """
        Метод ініціалізації класу, його властивостей і наповнення його елементами структури, переданої в параметрі args
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """
        Повертає кількість елементів структури
        :return: Кількість елементів
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Повертає перелік і зміст елементів структури у вигляді рядка
        :return: Рядок зі значеннями елементів структури
        """
        pass

    @abstractmethod
    def insert(self, value: Employee) -> None:
        """
        Метод вставки нового елемента структури в кінець, якщо це передбачено логікою структури
        :param value: Значення нового елемента структури
        :return: None
        """
        pass

    @abstractmethod
    def find(self, value: Employee) -> bool:
        """
        Метод пошуку значення в структурі з поверненням її індексу
        :param value: Значення елемента, що шукається
        :return: Позиція знайденого значення або IndexError
        """
        pass

    @abstractmethod
    def remove(self, value: Employee) -> None:
        """
        Метод видалення вказаного значення зі структури з сувом наступних елементів
        :param value: Значення, що видаляється з структури
        :return: None або ValueError
        """
        pass

    @abstractmethod
    def min(self) -> Employee:
        """
        Повертає найменший елемент структури
        :return: Значення найменшого елемента структури
        """
        pass


class AbstractTreeExtended(AbstractTreeBasic):
    # Розширений набір методів

    @abstractmethod
    def clear(self) -> None:
        """
        Метод видалення всіх елементів структури
        :return: None
        """
        pass

    @abstractmethod
    def replace(self, oldvalue: Employee, newvalue: Employee) -> None:
        """
        Метод заміни значення на нове
        :param oldvalue: Значення елемента, що шукається
        :param newvalue: Значення нового елементу
        :return: None або ValueError
        """
        pass

    @abstractmethod
    def __iter__(self) -> Iterable:
        """
        ПОвертає об'єкт-ітератор
        :return: Об'єкт-ітератор
        """
        pass

    @abstractmethod
    def __next__(self) -> Employee:
        """
        Метод визначає правила перебору елементів структури і наступний елемент
        :return: Наступний елемент  структури або виключення StopIteration, якщо всі перераховано
        """
        pass

    @abstractmethod
    def extend(self, values: Iterable[Employee]) -> None:
        """
        Метод вставки сукупності елементів з вказаної структури
        :param values: Структура, елементи якої додаються в поточну
        :return: None
        """
        pass

    @abstractmethod
    def count(self, value: Employee) -> int:
        """
        Метод підрахунку кількості включень заданого значення в структурі
        :param value: Значення, що шукається
        :return: Кількість включень заданого елемента
        """
        pass

class AbstractTreeBonus(AbstractTreeExtended):
    # Бонусний набір методів


    @abstractmethod
    def max(self) -> Employee:
        """
        Повертає найбільший елемент структури
        :return: Значення найбільшого елемента структури
        """
        pass

    @abstractmethod
    def __add__(self, other) -> AbstractTreeBasic|list:
        """
        Поєднання елементів поточної і наступної структури у єдину
        :param other: Структура, що поєднується з поточною
        :return: Структура зі значеннями обох структур, що поєднуються
        """
        pass

    @abstractmethod
    def __mul__(self, other) -> AbstractTreeBasic|list:
        """
        Дублювання елементів структури вказану кількість разів (тільки при множенні на ціле число), якщо це передбачено логікою структури
        :param other: Структура або число повторень
        :return: Структура з повтореннями вказаної кількості разів
        """
        pass

    def traversal(self) -> list[Employee]:
        """
        Обхід двійкового дерева одним з методів (pre-, in-, post-order) обходу в глубину або ширину
        :return: Список елементів структури
        """
        pass