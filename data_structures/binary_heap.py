from typing import Any, Union


class BinaryHeap:
    def __init__(self, *, return_max=False):
        self.__items = [None]
        self.__return_max = return_max

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

    def __swim(self, index):
        items = self.__items
        first_child = items[index // 2]
        second_child = items[index]

        if not self.__return_max:
            first_child, second_child = second_child, first_child

        while index > 1 and first_child < second_child:
            self.__swap_elements(index, index // 2)

            index //= 2
            first_child = items[index // 2]
            second_child = items[index]

            if not self.__return_max:
                first_child, second_child = second_child, first_child

    def __sink(self, index) -> None:
        items = self.__items

        while 2 * index < len(items):
            child_min_index = 2 * index

            first_child = items[child_min_index]

            if child_min_index == len(items) - 1:
                second_child = first_child
            else:
                second_child = items[child_min_index + 1]

            if not self.__return_max:
                first_child, second_child = second_child, first_child

            if (child_min_index < len(items) - 1) and first_child < second_child:
                child_min_index += 1

            first_child = items[index]
            second_child = items[child_min_index]

            if not self.__return_max:
                first_child, second_child = second_child, first_child

            if first_child >= second_child:
                break

            self.__swap_elements(index, child_min_index)
            index = child_min_index

    def __swap_elements(self, first, second):
        items = self.__items
        items[first], items[second] = items[second], items[first]

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

    binary_heap = BinaryHeap(return_max=True)

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

    binary_heap = BinaryHeap(return_max=False)

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
