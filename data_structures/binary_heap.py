from typing import Any, Union


class BinaryHeap:
    def __init__(self, items=Union[None, list]):
        self.__items = []

    def insert(self, item: Any) -> None:
        self.__items.append(item)
        self.__swim(len(self.__items) - 1)

    def del_max(self) -> Union[Any, None]:
        items = self.__items

        if len(items) <= 0:
            return

        items[0], items[len(items) - 1] = items[len(items) - 1], items[0]
        max_item = items.pop()

        self.__sink(0)
        return max_item

    def __swim(self, index):
        items = self.__items
        while index > 0 and items[index // 2] < items[index]:
            items[index], items[index // 2] = items[index // 2], items[index]
            index //= 2

    def __sink(self, index) -> None:
        items = self.__items
        while 2 * index <= len(items) - 1:
            j = 2 * index

            if j < len(items) - 1 and items[j] < items[j + 1]:
                j += 1

            if items[index] >= items[j]:
                break

            items[index], items[j] = items[j], items[index]
            index = j

    def __len__(self):
        return len(self.__items) - 1


if __name__ == '__main__':
    HEAP_ITEMS_QUANTITY = 5
    bh = BinaryHeap()
    for i in range(1, HEAP_ITEMS_QUANTITY + 1):
        bh.insert(i)

    bh.insert(132)
    for i in range(HEAP_ITEMS_QUANTITY + 1):
        print("max item =", bh.del_max())
