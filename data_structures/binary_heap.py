from typing import Any, Union


class BinaryHeap:
    def __init__(self, *, is_reverse_order=False, comparator=None):
        self.__items = [None]

        if comparator is None:
            comparator = self.__create_comparator()

        self.__comparator = comparator
        self.__controller = -1 if is_reverse_order else 1

    def insert(self, item: Any) -> None:
        self.__items.append(item)
        self.__swim(len(self.__items) - 1)

    def del_element(self) -> Union[Any, None]:
        items = self.__items

        if len(items) == 2:
            return items.pop()

        if len(items) <= 1:
            return

        items[1], items[len(items) - 1] = items[len(items) - 1], items[1]
        max_item = items.pop()

        self.__sink(1)
        return max_item

    def __swim(self, pointer):
        if pointer <= 1:
            return

        items = self.__items

        parent = items[pointer // 2]
        to_swim = items[pointer]

        while pointer > 1 and self.__comparator(parent, to_swim) == self.__controller:
            self.__swap_elements(pointer // 2, pointer)

            pointer //= 2

            parent = items[pointer // 2]
            to_swim = items[pointer]

    def __sink(self, index) -> None:
        items = self.__items
        while 2 * index <= len(items) - 1:
            j = 2 * index

            if j < len(items) - 1:
                if self.__comparator(items[j], items[j + 1]) == self.__controller:
                    j += 1

            if self.__comparator(items[index], items[j]) == -self.__controller:
                break

            items[index], items[j] = items[j], items[index]
            index = j

    def __swap_elements(self, first, second):
        items = self.__items
        items[first], items[second] = items[second], items[first]

    def __create_comparator(self):
        def default_comparator(a, b):
            if a > b:
                return 1
            if a < b:
                return -1
            return 0

        return default_comparator

    def __len__(self):
        return len(self.__items) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.__items) > 1:
            return self.del_element()
        raise StopIteration


if __name__ == '__main__':
    HEAP_ITEMS_QUANTITY = 10

    binary_heap = BinaryHeap(is_reverse_order=True)

    for i in range(1, HEAP_ITEMS_QUANTITY):
        binary_heap.insert(i)

    binary_heap.insert(132)
    binary_heap.insert(74)
    binary_heap.insert(282)
    binary_heap.insert(0)
    binary_heap.insert(-1)
    binary_heap.insert(100)

    print('Binary heap max order:')
    for element in binary_heap:
        print(element)
    print()

    binary_heap = BinaryHeap(is_reverse_order=False)

    for i in range(1, HEAP_ITEMS_QUANTITY):
        binary_heap.insert(i)

    binary_heap.insert(132)
    binary_heap.insert(74)
    binary_heap.insert(282)
    binary_heap.insert(0)
    binary_heap.insert(-1)
    binary_heap.insert(100)

    print('Binary heap min order:')
    for element in binary_heap:
        print(element)
