from typing import Any, Union


class Stack:
    """LIFO = "last in first out"""

    def __init__(self):
        self.__stack = []
        self.__last_element_index = 0
        self.__length = 0

    def push(self, value: Any) -> None:
        pass

    def pop(self) -> Union[None, Any]:
        pass

    def is_empty(self):
        pass

    def __len__(self) -> int:
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


if __name__ == '__main__':
    STACK_LENGTH = 5
    s = Stack()

    for i in range(1, STACK_LENGTH + 1):
        s.push(i)

