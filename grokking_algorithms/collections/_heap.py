from math import floor


class Heap():
    def __init__(self):
        self._items = []

    def insert(self, item, cap=None):
        self._items.append(item)
        self._heapify()

        if cap is not None:
            return [self.pop() for _ in range(len(self) - cap)]

    def pop(self):
        item = self._items.pop(0)
        self._heapify()
        return item
    
    def take(self, n):
        while n > 0 and any(self._items):
            yield self.pop()            
            n = n - 1

    def _heapify(self):
        size = len(self._items)
        index = size - 1
        value = self._items[index]

        while index > 0:
            parent_index = floor((index - 1) / 2)
            parent_value = self._items[parent_index]

            if parent_value < value:
                self._items[parent_index], self._items[index] = value, parent_value

            index = parent_index

    def __len__(self) -> int:
        return len(self._items)
