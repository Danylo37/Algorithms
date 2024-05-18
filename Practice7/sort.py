from Practice3.array import Array


class Sort(Array):

    def sort(self, reverse=False):
        self.__quicksort(0, len(self) - 1, reverse)

    def __quicksort(self, low, high, reverse):
        if low < high:
            pivot_index = self.__partition(low, high, reverse)
            self.__quicksort(low, pivot_index - 1, reverse)
            self.__quicksort(pivot_index + 1, high, reverse)

    def __partition(self, low, high, reverse):
        pivot = self[high]
        i = low - 1
        for j in range(low, high):
            if (self[j] > pivot) if reverse else (self[j] < pivot):
                i += 1
                self[i], self[j] = self[j], self[i]
        self[i + 1], self[high] = self[high], self[i + 1]
        return i + 1

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
