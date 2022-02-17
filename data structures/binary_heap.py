from typing import Any, Union


class BinaryHeap:
    def __init__(self):
        self.__items = []

    def insert(self, item: Any) -> None:
        self.__items.append(item)
        self.__swim(len(self.__items) - 1)

    def del_max(self) -> Union[Any, None]:
        pass

    def __swim(self, index):
        items = self.__items
        while index > 1 and items[index // 2] > items[index]:
            items[index], items[index // 2] = items[index // 2], items[index]
            index //= 2

    def __sink(self):
        pass

    def __len__(self):
        return len(self.__items)


if __name__ == '__main__':
    HEAP_ITEMS_QUANTITY = 10
    bh = BinaryHeap()
    for i in range(HEAP_ITEMS_QUANTITY):
        bh.insert(i)

    print(len(bh))
