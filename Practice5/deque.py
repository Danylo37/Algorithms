from Practice5.abstractlimitstructure import AbstractDeque
from Practice4.doublelinkedlist import DoubleLinkedList
from Practice1.abstract_object import Employee


class Deque(AbstractDeque):

    def __init__(self):
        self.__list = DoubleLinkedList()

    def push_first(self, value: Employee) -> None:
        if len(self.__list) == 0:
            self.__list.append(value)
            return
        self.__list.insert(0, value)

    def push_last(self, value: Employee) -> None:
        self.__list.append(value)

    def pop_first(self) -> Employee:
        if len(self.__list) == 0:
            raise IndexError("Deque is empty")
        return self.__list.pop(0)

    def pop_last(self) -> Employee:
        if len(self.__list) == 0:
            raise IndexError("Deque is empty")
        return self.__list.pop(len(self.__list) - 1)

    def top_first(self) -> Employee:
        if len(self.__list) == 0:
            raise IndexError("Deque is empty")
        return self.__list[0]

    def top_last(self) -> Employee:
        if len(self.__list) == 0:
            raise IndexError("Deque is empty")
        return self.__list[len(self.__list) - 1]

    def __repr__(self) -> str:
        return self.__list.__repr__()

    def __len__(self) -> int:
        return len(self.__list)
