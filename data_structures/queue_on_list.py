from data_structures.node import Node
from typing import Any, Union


class Queue:
    def __init__(self):
        self.__first_node = None
        self.__last_node = None
        self.__length = 0

    def enqueue(self, item: Any) -> None:
        self.__length += 1

        new_node = Node()
        new_node.item = item
        if self.__last_node is None:
            self.__first_node = new_node
            self.__last_node = new_node
            return

        self.__last_node.next_node = new_node
        self.__last_node = new_node

    def dequeue(self) -> Union[None, Node]:
        if self.__length == 0:
            return None

        self.__length -= 1

        old_first_node = self.__first_node
        self.__first_node = self.__first_node.next_node

        old_first_node.next = None
        return old_first_node.item

    def __len__(self):
        return self.__length

    def __iter__(self):
        return self

    def __next__(self):
        if self.__length <= 0:
            raise StopIteration
        return self.dequeue()


if __name__ == '__main__':
    QUEUE_LENGTH = 5
    q = Queue()

    for i in range(1, QUEUE_LENGTH + 1):
        q.enqueue(i)

    print(len(q))

    for item in q:
        print(item)
