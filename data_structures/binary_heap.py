from typing import Any, Union


class BinaryHeap:
    def __init__(self, return_max=False):
        self.__items = []
        self.__return_max = return_max

    def insert(self, item: Any) -> None:
        self.__items.append(item)
        self.__swim(len(self.__items) - 1)

    def del_element(self) -> Union[Any, None]:
        items = self.__items

        if len(items) <= 0:
            return

        items[0], items[len(items) - 1] = items[len(items) - 1], items[0]
        max_item = items.pop()

        self.__sink(0)
        return max_item

    def __swim(self, index):
        items = self.__items
        a = items[index // 2]
        b = items[index]

        if not self.__return_max:
            a, b = b, a

        while index > 0 and a < b:
            items[index], items[index // 2] = items[index // 2], items[index]
            index //= 2
            a = items[index // 2]
            b = items[index]
            if not self.__return_max:
                a, b = b, a

    def __sink(self, index) -> None:
        items = self.__items

        while 2 * index < len(items) - 1:
            j = 2 * index

            a = items[j]
            b = items[j + 1]
            if not self.__return_max:
                a, b = b, a

            if j < len(items) - 1 and a < b:
                j += 1

            a = items[index]
            b = items[j]
            if not self.__return_max:
                a, b = b, a

            if a >= b:
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
        print("max item =", bh.del_element())
