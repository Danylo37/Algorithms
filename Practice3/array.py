from Practice3.abstractstructure import AbstractStructureBonus, AbstractStructureBasic
from Practice1.employee import Employee
from typing import Iterable


class Array(AbstractStructureBonus):
    __array: list[Employee | None]
    __size: int
    __full_size: int

    def __init__(self, *args: Iterable[Employee]):
        if args:
            self.__array = [*args]
            self.__size = self.__get_size()
            self.__full_size = self.__size
        else:
            self.__full_size = 16
            self.__array = [None] * self.__full_size
            self.__size = 0

    def __get_size(self):
        size = 0
        for _ in self.__array:
            size += 1
        return size

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        if self.__size == 0:
            return "[]"

        result = "["
        for i in range(self.__size):
            result += str(self.__array[i]) + ", "
        return result[:-2] + "]"

    def __getitem__(self, key) -> list[Employee | None]:
        if not (isinstance(key, int) or isinstance(key, slice)):
            raise TypeError("Type must be int or slice")
        if isinstance(key, int) and key >= self.__size:
            raise IndexError("Index out of range")

        if isinstance(key, slice):
            if key.step is None or key.step >= 0:
                if key.stop is None:
                    key = slice(key.start, self.__size, key.step)
                elif key.stop > self.__size:
                    raise IndexError("Index out of range")
            else:
                if key.start is None:
                    key = slice(
                        self.__size - 1 if key.start is None else key.start, key.stop, key.step)
                elif key.start > self.__size - 1:
                    raise IndexError("Index out of range")
        return self.__array[key]

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key < self.__size:
            self.__array[key] = value
            return
        raise IndexError("Index out of range")

    def append(self, value: Employee) -> None:
        if self.__size == self.__full_size:
            self.__extend_size()
        self.__array[self.__size] = value
        self.__size += 1

    def __extend_size(self):
        self.__full_size *= 2
        temp = [None] * self.__full_size

        for i in range(self.__size):
            temp[i] = self.__array[i]
        self.__array = temp

    def insert(self, index: int, value: Employee) -> None:
        if index < 0 or index >= self.__size:
            raise IndexError("Index out of range")

        if self.__size == self.__full_size:
            self.__extend_size()

        for i in range(self.__size - 1, index - 1, -1):
            self.__array[i + 1] = self.__array[i]
        self.__array[index] = value
        self.__size += 1

    def index(self, value: Employee, start: int = 0, stop: int = -1) -> int:
        if stop == -1:
            stop = self.__size

        for i in range(start, stop):
            if self.__array[i] == value:
                return i
        raise ValueError("Value is not exists")

    def remove(self, value: Employee) -> None:
        index = self.index(value)
        for i in range(index, self.__size - 1):
            self.__array[i] = self.__array[i + 1]
        self.__array[self.__size - 1] = None
        self.__size -= 1

    def clear(self) -> None:
        for i in range(self.__size):
            self.__array[i] = None
        self.__size = 0

    def copy(self) -> list[Employee]:
        return self.__array[:self.__size]

    def __iter__(self) -> Iterable:
        self.__iter_index = 0
        return self

    def __next__(self) -> Employee:
        if self.__iter_index < self.__size:
            item = self.__array[self.__iter_index]
            self.__iter_index += 1
            return item
        else:
            raise StopIteration

    def __delitem__(self, key) -> None:
        if isinstance(key, int) and 0 <= key < self.__size:
            for i in range(key, self.__size - 1):
                self.__array[i] = self.__array[i + 1]
            self.__array[self.__size - 1] = None
            self.__size -= 1
        else:
            raise IndexError("Index out of range")

    def extend(self, values: Iterable[Employee]) -> None:
        for value in values:
            self.append(value)

    def pop(self, index: int) -> Employee:
        if isinstance(index, int) and 0 <= index < self.__size:
            popped_item = self.__array[index]
            del self.__array[index]
            self.__size -= 1
            return popped_item
        else:
            raise IndexError("Index out of range")

    def reverse(self) -> None:
        reverse_i = self.__size - 1
        for i in range(self.__size // 2):
            self.__array[i], self.__array[reverse_i] = self.__array[reverse_i], self.__array[i]
            reverse_i -= 1

    def count(self, value: Employee) -> int:
        count = 0
        for i in self:
            if i == value:
                count += 1
        return count

    def deepcopy(self) -> list[Employee] | AbstractStructureBasic:
        copied_array = Array()
        for i in self:
            e = Employee(i.name, i.surname, i.birthday, i.experience, i.position, i.salary)
            copied_array.append(e)
        return copied_array

    def min(self) -> Employee | None:
        if self.__size == 0:
            return None

        min_element = self.__array[0]
        for i in self:
            if i <= min_element:
                min_element = i
        return min_element

    def max(self) -> Employee | None:
        if self.__size == 0:
            return None

        max_element = self.__array[0]
        for i in self:
            if i >= max_element:
                max_element = i
        return max_element

    def __add__(self, other) -> AbstractStructureBasic | list:
        if not isinstance(other, Array):
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))

        combined_array = self.deepcopy()
        for item in other:
            combined_array.append(item)
        return combined_array

    def __mul__(self, other) -> AbstractStructureBasic | list:
        if not isinstance(other, int):
            raise TypeError("can't multiply sequence by non-int of type '{}'".format(type(other)))
        if other < 0:
            raise ValueError("Can't multiply by negative number")
        duplicated_array = Array()
        for _ in range(other):
            for item in self:
                duplicated_array.append(item)
        return duplicated_array
