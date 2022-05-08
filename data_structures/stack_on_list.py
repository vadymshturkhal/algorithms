from typing import Any, Union


class Stack:
    """LIFO = "last in first out"""

    def __init__(self):
        self.__stack = []
        self.__last_element_index = 0

    def push(self, value: Any) -> None:
        self.__stack.append(value)
        self.__last_element_index += 1

    def pop(self) -> Union[None, Any]:
        if self.is_empty(): return

        value_to_return = self.__stack[self.__last_element_index]
        self.__stack[self.__last_element_index] = None
        self.__last_element_index -= 1
        return value_to_return


    def is_empty(self):
        return self.__last_element_index == 0

    def __len__(self) -> int:
        return self.__last_element_index

    def __iter__(self):
        pass

    def __next__(self):
        pass


if __name__ == '__main__':
    STACK_LENGTH = 5
    s = Stack()

    for i in range(1, STACK_LENGTH + 1):
        s.push(i)
    
    print("Stack length =", len(s))

    for i in range(1, STACK_LENGTH + 1):
        print(s.pop())

