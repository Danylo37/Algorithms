from Practice3.array import Array
from typing import Iterable


class Sort(Array, Iterable):

    def sort(self, reverse=False):
        n = len(self)
        width = 1
        while width < n:
            for i in range(0, n, 2 * width):
                self.__merge(i, min(i + width, n), min(i + 2 * width, n))
            width *= 2
        if reverse:
            self.reverse()

    def __merge(self, start, mid, end):
        merged = Sort()
        left, right = start, mid
        while left < mid and right < end:
            if self[left] <= self[right]:
                merged.append(self[left])
                left += 1
            else:
                merged.append(self[right])
                right += 1
        while left < mid:
            merged.append(self[left])
            left += 1
        while right < end:
            merged.append(self[right])
            right += 1
        for i, val in enumerate(merged):
            self[start + i] = val

    def sort_by_attr(self, attr: str, reverse=False):
        for i in range(1, len(self)):
            key_item = self[i]
            key_value = getattr(key_item, attr)
            j = i - 1
            while (j >= 0
                   and ((getattr(self[j], attr) < key_value) if reverse else (getattr(self[j], attr) > key_value))):
                self[j + 1] = self[j]
                j -= 1
            self[j + 1] = key_item

    def sort_by_lambda(self, func):
        for i in range(len(self) - 1, 0, -1):
            for k in range(0, i):
                if func(self[k], self[k+1]):
                    self[k], self[k+1] = self[k+1], self[k]
