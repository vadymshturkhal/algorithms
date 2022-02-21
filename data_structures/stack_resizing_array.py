from typing import Any, Union


class StackResizingArray:
    def __init__(self):
        self.__data = [None]
        self.__length = 0

    def push(self, item: Any) -> None:
        if self.__length == len(self.__data):
            self.__resize_array(self.__length * 2)

    def pop(self) -> Union[None, Any]:
        pass

    def __resize_array(self, capacity):
        temp_array = [None] * capacity
        for i in range(len(self.__data)):
            temp_array[i] = self.__data[i]
        self.__data = temp_array

    def __len__(self) -> int:
        return self.__length


if __name__ == '__main__':
    STACK_LENGTH = 5
    s = StackResizingArray()

    print("Stack length =", len(s))
