from typing import Any, Union


class Stack:
    """LIFO = "last in first out"""

    def __init__(self):
        self.__stack = []

    def push(self, value: Any) -> None:
        self.__stack.append(value)

    def pop(self) -> Union[None, Any]:
        if self.is_empty(): return

        return self.__stack.pop()


    def is_empty(self):
        return len(self.__stack) == 0

    def __len__(self) -> int:
        return len(self.__stack)

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty():
            raise StopIteration

        return self.__stack.pop()


if __name__ == '__main__':
    STACK_LENGTH = 5
    s = Stack()

    for i in range(1, STACK_LENGTH + 1):
        s.push(i)
    print('pop()')
    print("Stack length =", len(s))

    for i in range(1, STACK_LENGTH + 1):
        print(s.pop())
    print(f'{s.is_empty()=}')
    print(f'{s.pop()=}')
    print()

    print('for...in')
    for i in range(1, STACK_LENGTH + 1):
        s.push(i)
    print("Stack length =", len(s))
    for val in s:
        print(val)
    print(f'{s.pop()=}')
