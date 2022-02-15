from typing import Any


class Node:
    """Node for data structures"""

    def __init__(self):
        self.__item = None
        self.__forward = None
        self.__previous = None

    @property
    def item(self) -> Any:
        return self.__item

    @item.setter
    def item(self, item: Any) -> None:
        self.__item = item

    @property
    def next_node(self) -> None:
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


