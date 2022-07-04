from typing import Any
from copy import deepcopy


class Node:
    """Node for data_structures"""

    def __init__(self, key=None, value=None, color=None, count=0):
        self.__key = key
        self.__item = value
        self.__forward = None
        self.__previous = None
        self.__color = color
        self.__count = count
        self.__neighbours = None

    def add_neigbours(self, neigbours):
        if self.__neighbours is None:
            self.__neighbours = []

        for neghbour in neigbours:
            self.__neighbours.append(neghbour)
    
    def get_neighbours(self):
        return deepcopy(self.__neighbours)

    @property
    def key(self) -> Any:
        return self.__key

    @key.setter
    def key(self, value: Any):
        self.__key = value

    @property
    def value(self) -> Any:
        return self.__item

    @value.setter
    def value(self, value) -> None:
        self.__item = value

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
