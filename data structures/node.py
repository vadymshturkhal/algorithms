from typing import Any


class Node:
    """Node for data structures"""

    def __init__(self):
        self.__item = None
        self.__forward = None
        self.__previous = None

    def add_item(self, item: Any) -> None:
        self.__item = item

    def retrieve_item(self) -> Any:
        return self.__item

    def add_next(self, n: 'Node') -> None:
        self.__forward = n

    def add_previous(self, n: 'Node') -> None:
        self.__previous = n

