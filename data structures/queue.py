from typing import Any


class Queue:
    def __init__(self):
        self.__length = 0

    def enqueue(self, item: Any):
        pass

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
