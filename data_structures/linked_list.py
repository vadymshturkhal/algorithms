from data_structures.node import Node


class LinkedList:
    def __init__(self) -> None:
        self.__first = None
        self.__current = None
        self.__length = 0

    def search(self, value) -> [None, Node]:
        """Returns Node or None"""
        cur = self.__first

        while cur is not None:
            if cur.item == value:
                return cur

            cur = cur.next_node

        return

    def insert(self, value) -> None:
        if self.is_empty():
            self.__first = Node(value=value)
            self.__current = self.__first
            self.__length += 1
            return

        current = Node(value=value)
        current.previous = self.__current
        self.__current.next_node = current
        self.__current = current

    def delete(self, value):
        pass

    def is_empty(self):
        return self.__length == 0

    def __len__(self):
        return self.__length

    def __str__(self):
        cur = self.__first

        values = []
        while cur is not None:
            values.append(cur.item)
            cur = cur.next_node

        return f'{values}'


if __name__ == '__main__':
    LIST_SIZE = 5
    l_l = LinkedList()

    for i in range(1, LIST_SIZE + 1):
        l_l.insert(i)

    n = l_l.search(3)
    n.item = 11
    print(l_l)
