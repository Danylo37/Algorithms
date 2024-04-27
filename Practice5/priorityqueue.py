from Practice5.abstractlimitstructure import AbstractQueue
from Practice1.employee import Employee
from Practice3.array import Array


class PriorityQueue(AbstractQueue):

    def __init__(self):
        self.__array = Array()

    def enqueue(self, value: Employee) -> None:
        if len(self.__array) == 0:
            self.__array.append(value)
            return

        for i in range(len(self.__array)):
            if self.__array[i] > value:
                self.__array.insert(i, value)
                return
        self.__array.append(value)

    def dequeue(self) -> Employee:
        if len(self.__array) == 0:
            raise IndexError("Deque is empty")

        return self.__array.pop(0)

    def top(self) -> Employee:
        if len(self.__array) == 0:
            raise IndexError("Deque is empty")
        return self.__array[0]

    def __repr__(self) -> str:
        return self.__array.__repr__()

    def __len__(self) -> int:
        return len(self.__array)
