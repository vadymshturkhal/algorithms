from node import Node
from typing import Any


class Stack:
    """LIFO = "last in first out"""

    def __init__(self):
        self.__last_node = None

    def push(self, item: Any):
        old_first_node = self.__last_node

        new_node = Node()
        new_node.add_previous(old_first_node)
        new_node.add_item(item)

        self.__last_node = new_node

    def pop(self):
        pass

    def __len__(self):
        return 0


if __name__ == '__main__':
    s = Stack()
    print(len(s))
