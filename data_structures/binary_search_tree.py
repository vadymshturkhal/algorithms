from typing import Any, Union
from data_structures.node import Node
from data_structures.queue import Queue


class BinarySearchTree:
    """
        Symmetric order.
        Each node has a key, and every node’s key is:
            1. Larger than all keys in its left subtree;
            2. Smaller than all keys in its right subtree.

        Node.previous = smaller,
        Node.next_node = greater.
    """

    def __init__(self):
        self.__root = None
        self.__iterable = None

    def put(self, key: Any, value: Any) -> None:
        self.__root = self.__put(self.__root, key, value)

    def get(self, key) -> Union[None, Any]:
        current_node = self.__root

        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return current_node.item

        return None

    def min(self, node: Node = None) -> Union[None, Node]:
        if node is None:
            cursor_node = self.__root
        else:
            cursor_node = node

        if cursor_node is None:
            return None

        # If len == 1
        if cursor_node.left is None:
            return cursor_node

        while True:
            cursor_node = cursor_node.left
            if cursor_node.left is None:
                break

        return cursor_node

    def delete_min(self, node: Node = None) -> Union[None, Node]:
        if node is None:
            cursor_node = self.__root
        else:
            cursor_node = node

        if cursor_node is None:
            return None

        # If len == 1
        if cursor_node.left is None:
            self.__root = self.__root.right
            return None

        while True:
            prev_node = cursor_node
            cursor_node = cursor_node.left
            if cursor_node.left is None:
                prev_node.left = cursor_node.right
                break

        return cursor_node

    def delete_max(self) -> None:
        cursor_node = self.__root
        if cursor_node is None:
            return None

        # If len == 1
        if cursor_node.right is None:
            self.__root = self.__root.left
            return None

        while True:
            prev_node = cursor_node
            cursor_node = cursor_node.right
            if cursor_node.right is None:
                prev_node.right = cursor_node.left
                break

        return None

    def delete(self, key) -> None:
        """Hibbard deletion"""
        self.__root = self.__delete(self.__root, key)

    def __delete(self, n: Node, key: Any) -> Union[None, Node]:
        if n is None:
            return None

        if key < n.key:
            n.left = self.__delete(n.left, key)
        elif key > n.key:
            n.right = self.__delete(n.right, key)
        else:
            if n.right is None:
                return n.left
            if n.left is None:
                return n.right

            temp_node = n
            n = self.min(temp_node.right)
            n.right = self.delete_min(temp_node.right)
            n.left = temp_node.left
        return n

    def __put(self, node: Node, key: Any, value: Any) -> Node:
        if node is None:
            return Node(key, value)

        if key < node.key:
            node.left = self.__put(node.left, key, value)
        elif key > node.key:
            node.right = self.__put(node.right, key, value)
        else:
            node.item = value

        return node

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
    bst = BinarySearchTree()

    keys = [2, 1, 3, 5, 8, 4, 12]
    for k in keys:
        bst.put(k, k)

    # for item in bst:
    #     print(item)
    #
    # print()
    # print('min =', bst.min().key)
    # print('After delete_min')
    # print('min =', bst.delete_min().key)
    # for item in bst:
    #     print(item)
    #
    # print()
    # print('After delete_max')
    # bst.delete_max()
    # for item in bst:
    #     print(item)

    # print()
    print('After delete 5')
    bst.delete(5)
    for item in bst:
        print(item)
