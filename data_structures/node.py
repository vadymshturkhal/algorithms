from typing import Any


class Node:
    """Node for data_structures"""

    def __init__(self, key=None, value=None, color=None):
        self.__key = key
        self.__item = value
        self.__forward = None
        self.__previous = None
        self.__color = None
        self.__count = 0

    @property
    def key(self) -> Any:
        return self.__key

    @key.setter
    def key(self, value: Any):
        self.__key = value

    @property
    def item(self) -> Any:
        return self.__item

    @item.setter
    def item(self, item: Any) -> None:
        self.__item = item

    @property
    def next_node(self) -> 'Node':
        return self.__forward

    @next_node.setter
    def next_node(self, n: 'Node') -> None:
        self.__forward = n

    @property
    def previous(self) -> 'Node':
        return self.__previous

    @previous.setter
    def previous(self, n: 'Node') -> None:
        self.__previous = n

    @property
    def left(self) -> 'Node':
        return self.__previous

    @left.setter
    def left(self, n: 'Node') -> None:
        self.__previous = n

    @property
    def right(self) -> 'Node':
        return self.__forward

    @right.setter
    def right(self, n: 'Node') -> None:
        self.__forward = n

    @property
    def color(self) -> bool:
        return self.__color

    @color.setter
    def color(self, value: bool):
        self.__color = value

    @property
    def count(self) -> int:
        return self.__count

    @count.setter
    def count(self, value: int) -> None:
        self.__count = value
