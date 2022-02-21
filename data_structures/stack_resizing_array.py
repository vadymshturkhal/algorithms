from typing import Any, Union


class StackResizingArray:
    def __init__(self):
        self.__data = [None]
        self.__length = 0

    def push(self, item: Any) -> None:
        if self.__length == len(self.__data):
            self.__resize_array(self.__length * 2)

        self.__data[self.__length] = item
        self.__length += 1

    def pop(self) -> Union[None, Any]:
        length = self.__length - 1

        temp_item = self.__data[length]
        self.__data[length] = None
        self.__length -= 1

        if self.__length > 0 and self.__length == len(self.__data) // 4:
            self.__resize_array(len(self.__data) // 2)

        return temp_item

    def __resize_array(self, capacity):
        temp_array = [None] * capacity
        for i in range(self.__length):
            temp_array[i] = self.__data[i]
        self.__data = temp_array

    def __len__(self) -> int:
        return self.__length


if __name__ == '__main__':
    STACK_LENGTH = 10
    s = StackResizingArray()

    for i in range(1, STACK_LENGTH + 1):
        s.push(i)

    print("Stack length =", len(s))

    for i in range(1, STACK_LENGTH + 1):
        print(s.pop())
    print("Stack length =", len(s))
