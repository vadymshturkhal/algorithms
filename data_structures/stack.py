from node import Node
from typing import Any, Union


class Stack:
    """LIFO = "last in first out"""

    def __init__(self):
        self.__last_node = None
        self.__length = 0

    def push(self, item: Any):
        old_last_node = self.__last_node

        new_node = Node()
        new_node.previous = old_last_node
        new_node.item = item

        self.__last_node = new_node
        self.__length += 1

    def pop(self) -> Union[None, Node]:
        if self.__length == 0:
            return None

        current_last_node = self.__last_node
        self.__last_node = current_last_node.previous
        current_last_node.previous = None

        self.__length -= 1
        return current_last_node.item

    def __len__(self) -> int:
        return self.__length

    def __iter__(self):
        return self

    def __next__(self):
        if self.__length <= 0:
            raise StopIteration

        return self.pop()


if __name__ == '__main__':
    STACK_LENGTH = 5
    s = Stack()

    for i in range(1, STACK_LENGTH + 1):
        s.push(i)

    print("Stack length =", len(s))

    for item in s:
        print(f"{item = }")
