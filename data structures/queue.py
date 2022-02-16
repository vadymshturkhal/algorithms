from node import Node
from typing import Any


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

    def dequeue(self):
        pass

    def __len__(self):
        return self.__length


if __name__ == '__main__':
    QUEUE_LENGTH = 5
    q = Queue()

    for i in range(QUEUE_LENGTH):
        q.enqueue(i)

    print(len(q))

    for i in range(QUEUE_LENGTH):
        print(q.dequeue())
