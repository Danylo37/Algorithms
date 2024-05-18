from Practice3.abstractstructure import AbstractStructureBonus, AbstractStructureBasic
from Practice1.employee import Employee
from typing import Iterable


class Array(AbstractStructureBonus):
    _array: list[Employee | None]
    _size: int
    _full_size: int

    def __init__(self, *args: Iterable[Employee]):
        if args:
            self._array = [*args]
            self._size = self.__get_size()
            self._full_size = self._size
        else:
            self._full_size = 16
            self._array = [None] * self._full_size
            self._size = 0

    def __get_size(self):
        size = 0
        for _ in self._array:
            size += 1
        return size

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        if self._size == 0:
            return "[]"

        result = "["
        for i in range(self._size):
            result += str(self._array[i]) + ", "
        return result[:-2] + "]"

    def __getitem__(self, key) -> list[Employee] | Employee:
        if not (isinstance(key, int) or isinstance(key, slice)):
            raise TypeError("Type must be int or slice")
        if isinstance(key, int) and key >= self._size:
            raise IndexError("Index out of range")

        if isinstance(key, slice):
            if key.step is None or key.step >= 0:
                if key.stop is None:
                    key = slice(key.start, self._size, key.step)
                elif key.stop > self._size:
                    raise IndexError("Index out of range")
            else:
                if key.start is None:
                    key = slice(
                        self._size - 1 if key.start is None else key.start, key.stop, key.step)
                elif key.start > self._size - 1:
                    raise IndexError("Index out of range")
        return self._array[key]

    def __setitem__(self, key, value):
        if isinstance(key, int) and 0 <= key < self._size:
            self._array[key] = value
            return
        raise IndexError("Index out of range")

    def append(self, value: Employee) -> None:
        if self._size == self._full_size:
            self._extend_size()
        self._array[self._size] = value
        self._size += 1

    def _extend_size(self):
        self._full_size *= 2
        temp = [None] * self._full_size

        for i in range(self._size):
            temp[i] = self._array[i]
        self._array = temp

    def insert(self, index: int, value: Employee) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        if self._size == self._full_size:
            self._extend_size()

        for i in range(self._size - 1, index - 1, -1):
            self._array[i + 1] = self._array[i]
        self._array[index] = value
        self._size += 1

    def index(self, value: Employee, start: int = 0, stop: int = -1) -> int:
        if stop == -1:
            stop = self._size

        for i in range(start, stop):
            if self._array[i] == value:
                return i
        raise ValueError("Value is not exists")

    def remove(self, value: Employee) -> None:
        index = self.index(value)
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._array[self._size - 1] = None
        self._size -= 1

    def clear(self) -> None:
        for i in range(self._size):
            self._array[i] = None
        self._size = 0

    def copy(self) -> list[Employee]:
        return self._array[:self._size]

    def __iter__(self):
        self.__iter_index = 0
        return self

    def __next__(self) -> Employee:
        if self.__iter_index < self._size:
            item = self._array[self.__iter_index]
            self.__iter_index += 1
            return item
        else:
            raise StopIteration

    def __delitem__(self, key) -> None:
        if isinstance(key, int) and 0 <= key < self._size:
            for i in range(key, self._size - 1):
                self._array[i] = self._array[i + 1]
            self._array[self._size - 1] = None
            self._size -= 1
        else:
            raise IndexError("Index out of range")

    def extend(self, values: Iterable[Employee]) -> None:
        for value in values:
            self.append(value)

    def pop(self, index: int) -> Employee:
        if isinstance(index, int) and 0 <= index < self._size:
            popped_item = self._array[index]
            del self._array[index]
            self._size -= 1
            return popped_item
        else:
            raise IndexError("Index out of range")

    def reverse(self) -> None:
        reverse_i = self._size - 1
        for i in range(self._size // 2):
            self._array[i], self._array[reverse_i] = self._array[reverse_i], self._array[i]
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
        if self._size == 0:
            return None

        min_element = self._array[0]
        for i in self:
            if i <= min_element:
                min_element = i
        return min_element

    def max(self) -> Employee | None:
        if self._size == 0:
            return None

        max_element = self._array[0]
        for i in self:
            if i >= max_element:
                max_element = i
        return max_element

    def __add__(self, other) -> AbstractStructureBasic:
        if not isinstance(other, Array):
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))

        combined_array = self.deepcopy()
        for item in other:
            combined_array.append(item)
        return combined_array

    def __mul__(self, other) -> AbstractStructureBasic:
        if not isinstance(other, int):
            raise TypeError("can't multiply sequence by non-int of type '{}'".format(type(other)))
        if other < 0:
            raise ValueError("Can't multiply by negative number")
        duplicated_array = Array()
        for _ in range(other):
            for item in self:
                duplicated_array.append(item)
        return duplicated_array
