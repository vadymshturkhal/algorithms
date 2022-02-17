from typing import Any, Union


class UnorderedMaxPriorityQueue:
    def __init__(self):
        self.__items = []

    def insert(self, item: Any) -> None:
        self.__items.append(item)

    def delete_max(self) -> Union[Any, None]:
        if len(self.__items) == 0:
            return

        length = len(self.__items)
        max_item_index = 0
        for current_index in range(1, length):
            current_item = self.__items[current_index]

            if current_item > self.__items[max_item_index]:
                max_item_index = current_index

        self.__items[max_item_index], self.__items[length - 1] = self.__items[length - 1], self.__items[max_item_index]

        return self.__items.pop()

    def __len__(self):
        return len(self.__items)


if __name__ == '__main__':
    unordered_max_pq = UnorderedMaxPriorityQueue()
    ITEMS_LENGTH = 10
    for i in range(ITEMS_LENGTH, 0, -1):
        unordered_max_pq.insert(i)

    print(unordered_max_pq.delete_max())
    print(unordered_max_pq.delete_max())
    print(unordered_max_pq.delete_max())
