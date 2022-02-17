from typing import Any


class UnorderedMaxPriorityQueue:
    def __init__(self):
        self.__length = 0
        self.__items = []

    def insert(self, item: Any) -> None:
        self.__items.append(item)

    def delete_max(self) -> Any:
        pass

    def __len__(self):
        return self.__length


if __name__ == '__main__':
    pass
