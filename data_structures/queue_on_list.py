from typing import Any, Union


class Queue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, value: Any) -> None:
        self.__queue.insert(0, value)

    def dequeue(self) -> Union[None, Any]:
        if self.is_empty():
            return

        return self.__queue.pop(0)

    def is_empty(self) -> bool:
        return len(self.__queue) == 0

    def __len__(self):
        return len(self.__queue)

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty():
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
