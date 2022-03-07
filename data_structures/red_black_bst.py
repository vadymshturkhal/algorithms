from typing import Union, Any
from data_structures.node import Node
from data_structures.queue import Queue


class RedBlackBST:
    def __init__(self):
        self.__RED = True
        self.__BLACK = False
        self.__root = None
        self.__iterable = None

    def get(self, key) -> Union[None, Any]:
        """
            Search is the same as for elementary BST (ignore color).
            But runs faster because of better balance.
        """
        current_node = self.__root

        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return current_node.item

        return None

    def put(self, key: Any, value: Any) -> None:
        self.__root = self.__put(self.__root, key, value)

    def __put(self, node: Node, key: Any, value: Any) -> Node:
        if node is None:
            return Node(key, value)

        if key < node.key:
            node.left = self.__put(node.left, key, value)
        elif key > node.key:
            node.right = self.__put(node.right, key, value)
        else:
            node.item = value

        if self.__is_red(node.right) and not self.__is_red(node.left):
            self.__rotate_left(node)

        if self.__is_red(node.left) and self.__is_red(node.left.left):
            self.__rotate_right(node)

        if self.__is_red(node.left) and self.__is_red(node.right):
            self.__flip_colors(node)

        return node

    def __is_red(self, n: Node):
        if n is None:
            return False
        return n.color == self.__RED

    def __rotate_left(self, n: Node) -> Node:
        temp = n.right
        n.right = temp.left
        temp.left = n
        temp.color = n.color
        n.color = self.__RED
        return temp

    def __rotate_right(self, n: Node) -> Node:
        temp = n.left
        n.left = temp.right
        temp.right = n
        temp.color = n.color
        n.color = self.__RED
        return temp

    def __flip_colors(self, n: Node) -> None:
        n.color = self.__RED
        n.left.color = self.__BLACK
        n.right.color = self.__BLACK

    def __prepare_iterable(self, n: Node = None, q: Queue = None) -> None:
        if n is None:
            return
        self.__prepare_iterable(n.left, q)
        q.enqueue(n)
        self.__prepare_iterable(n.right, q)

    def __iter__(self):
        self.__iterable = Queue()
        self.__prepare_iterable(self.__root, self.__iterable)
        return self

    def __next__(self):
        for node in self.__iterable:
            return node.item
        raise StopIteration


if __name__ == '__main__':
    rb = RedBlackBST()

    keys = ['s', 'e', 'a', 'r', 'c', 'h', 'x', 'm', 'p', 'l']
    for k in keys:
        rb.put(k, k)

    print(*rb)
