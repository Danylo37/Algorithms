from Practice3.abstractstructure import AbstractStructureBonus
from Practice4.doublenode import DoubleNode
from Practice1.employee import Employee
from typing import Iterable


class DoubleLinkedList(AbstractStructureBonus):
    def __init__(self, *args: Iterable[Employee]) -> None:
        self.__head: None | DoubleNode = None
        self.__tail: None | DoubleNode = None
        self.__size = 0

        if args is not None:
            for arg in args:
                self.append(arg)

    def __len__(self) -> int:
        return self.__size

    def __repr__(self) -> str:
        content = ''
        current_node = self.__head
        while current_node is not None:
            content += str(current_node.data) + ', '
            current_node = current_node.next

        if len(content) > 1:
            content = content[:-2]

        return '[' + content + ']'

    def __getitem__(self, key) -> AbstractStructureBonus | Employee:
        if isinstance(key, slice):
            start = key.start if key.start is not None else 0
            stop = key.stop if key.stop is not None else self.__size
            step = key.step if key.step is not None else 1

            if start < 0:
                start += self.__size
            if stop < 0:
                stop += self.__size

            sliced_list = DoubleLinkedList()
            current_node = self.__head
            index = 0

            while current_node is not None and index < stop:
                if index >= start and (index - start) % step == 0:
                    sliced_list.append(current_node.data)
                current_node = current_node.next
                index += 1

            return sliced_list
        elif isinstance(key, int):
            if key < 0:
                key += self.__size

            if key < 0 or key >= self.__size:
                raise IndexError("Index out of range")

            current_node = self.__head
            for _ in range(key):
                current_node = current_node.next

            return current_node.data
        else:
            raise TypeError("Index must be an integer or slice")

    def __setitem__(self, key, value) -> None:
        if not isinstance(key, int):
            raise TypeError("Index must be an integer")

        if key < 0:
            key += self.__size

        if 0 <= key < self.__size:
            if value in self:
                return

            current = self.__head
            while self.index(current.data) != key:
                current = current.next
            current.data = value

        else:
            raise IndexError("Index out of range")

    def append(self, value: Employee | Iterable[Employee]) -> None:
        if value in self:
            return

        node = DoubleNode(value)

        if self.__head is None:
            self.__head = self.__tail = node

        else:
            self.__tail.next = node
            node.prev = self.__tail
            self.__tail = node

        self.__size += 1

    def __contains__(self, item) -> bool:
        try:
            if self.index(item) is not None:
                return True
        except ValueError:
            return False

    def insert(self, index: int, value: Employee) -> None:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer or slice")

        if index < 0:
            index += self.__size

        if 0 <= index < self.__size:
            if value in self:
                return

            node = DoubleNode(value)

            if index == 0:
                self.__head.prev = node
                node.next = self.__head
                self.__head = node

            elif index == self.__size - 1:
                self.__tail.next = node
                node.prev = self.__tail
                self.__tail = node

            else:
                current = self.__head.next
                while self.index(current.data) != index:
                    current = current.next
                node.next = current
                node.prev = current.prev
                current.prev.next = node
                current.prev = node

            self.__size += 1

        else:
            raise IndexError("Index out of range")

    def index(self, value: Employee, start: int = 0, stop: int = -1) -> int:
        if stop == -1:
            stop = self.__size

        for i in range(start, stop):
            if self[i] == value:
                return i
        raise ValueError(f"{value} is not in list")

    def remove(self, value: Employee) -> None:
        if value in self:
            if self.__head.data == value:
                if self.__head.next is not None:
                    self.__head = self.__head.next
                    self.__head.prev = None
                else:
                    self.__head = None
            elif self.__tail.data == value:
                self.__tail = self.__tail.prev
                self.__tail.next = None
            else:
                current = self.__head
                while current.data != value:
                    current = current.next
                current.prev.next = current.next
                current.next.prev = current.prev

            self.__size -= 1
        else:
            raise ValueError(f"{value} is not in list")

    def clear(self) -> None:
        for i in self:
            self.remove(i)

    def copy(self) -> AbstractStructureBonus:
        new_dll = DoubleLinkedList()
        for i in self:
            new_dll.append(i)
        return new_dll

    def __iter__(self) -> AbstractStructureBonus:
        self.__iter_node = self.__head
        return self

    def __next__(self) -> Employee:
        if self.__iter_node is not None:
            data = self.__iter_node.data
            self.__iter_node = self.__iter_node.next
            return data
        else:
            raise StopIteration

    def __delitem__(self, key) -> None:
        if not isinstance(key, int):
            raise TypeError("Index must be an integer or slice")

        if key < 0:
            key += self.__size

        if 0 <= key < self.__size:
            self.remove(self[key])
        else:
            raise IndexError("Index out of range")

    def extend(self, values: Iterable[Employee]) -> None:
        for value in values:
            self.append(value)

    def pop(self, index: int) -> Employee:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")

        if index < 0:
            index += self.__size

        if 0 <= index < self.__size:
            value = self[index]
            self.remove(value)
            return value
        else:
            raise IndexError("Index out of range")

    def reverse(self) -> None:
        if self.__size != 0:
            self.__tail = self.__head
            while self.__head.next:
                self.__head.next, self.__head.prev, self.__head = self.__head.prev, self.__head.next, self.__head.next

            self.__head.next, self.__head.prev = self.__head.prev, None

    def count(self, value: Employee) -> int:
        return 1 if value in self else 0

    def deepcopy(self) -> list[Employee] | AbstractStructureBonus:
        copied_dll = DoubleLinkedList()
        for i in range(self.__size):
            e = Employee(self[i].name, self[i].surname, self[i].birthday, self[i].experience, self[i].position,
                         self[i].salary)
            copied_dll.append(e)
        return copied_dll

    def min(self) -> Employee | None:
        if self.__size == 0:
            return None

        min_element = self[0]
        for i in self:
            if i < min_element:
                min_element = i
        return min_element

    def max(self) -> Employee | None:
        if self.__size == 0:
            return None

        min_element = self[0]
        for i in self:
            if i > min_element:
                min_element = i
        return min_element

    def __add__(self, other) -> AbstractStructureBonus:
        if not isinstance(other, DoubleLinkedList):
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))

        combined_dll = self.deepcopy()
        for item in other:
            combined_dll.append(item)
        return combined_dll

    def __mul__(self, other) -> AbstractStructureBonus:
        raise NotImplementedError("Multiplication operation is not supported for DoubleLinkedList without duplicates")
