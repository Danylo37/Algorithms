from Practice1.employee import Employee
from Practice3.array import Array
from typing import Iterable


class Find(Array, Iterable):

    def append(self, value: Employee) -> None:
        if self._size == self._full_size:
            self._extend_size()

        index = self._size
        for i in range(self._size - 1, -1, -1):
            if not self._array[i] or self._array[i] < value:
                break
            self._array[i + 1] = self._array[i]
            index = i
        self._array[index] = value
        self._size += 1

    def find(self, value: Employee) -> int | None:
        for (i, item) in enumerate(self):
            if item == value:
                return i
        return -1

    def find_by_attr(self, value: str, attr: str):
        for (i, item) in enumerate(self):
            if getattr(item, attr) == value:
                return i
        return -1

    def find_by_attrs(self, **values):
        for i, item in enumerate(self):
            if all(getattr(item, attr) == value for attr, value in values.items()):
                return i
        return -1

    def find_by_lambda(self, value: Employee, function):
        for (i, item) in enumerate(self):
            if function(item, value):
                return i
        return -1

    def exponential_search(self, value: Employee) -> int | None:
        if self[0] == value:
            return 0

        n = len(self)
        i = 1
        while i < n and self[i] <= value:
            i *= 2

        return self.__binary_search(value, i // 2, min(i, n - 1))

    def __binary_search(self, value, low, high):
        while low <= high:
            mid = (low + high) // 2
            if self[mid] < value:
                low = mid + 1
            elif self[mid] > value:
                high = mid - 1
            else:
                return mid
        return -1
