from typing import Any, Union
from data_structures.node import Node


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
        self.__count = 0

    def put(self, key: Any, item: Any) -> None:
        self.__root = self.__put(self.__root, key, item)

    def get(self, key) -> Union[None, Any]:
        current_node = self.__root

        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.previous
            elif key > current_node.key:
                current_node = current_node.next_node
            else:
                return current_node.item

        return None

    def size(self):
        return self.__size(self.__root)

    def rank(self, key: Any) -> int:
        return self.__rank(key, self.__root)

    def delete(self) -> None:
        pass

    def max(self) -> Node:
        pass

    def min(self) -> Node:
        pass

    def floor(self, key: Any) -> Any:
        """Largest key that is less than n"""
        temp = self.__floor(self.__root, key)

        if temp is None:
            return None

        return temp.key

    def ceiling(self) -> Node:
        pass

    def __put(self, node: Node, key: Any, item: Any) -> Node:
        if node is None:
            return Node(key, item)

        if key < node.key:
            node.left = self.__put(node.left, key, item)
        elif key > node.key:
            node.right = self.__put(node.right, key, item)
        else:
            node.item = item

        node.count = 1 + self.__size(node.left) + self.__size(node.right)

        return node

    def __floor(self, n: Node, key: Any) -> Union[None, Node]:
        if n is None:
            return None

        if key == n.key:
            return n

        if key < n.key:
            return self.__floor(n.left, key)

        temp = self.__floor(n.right, key)

        return n if temp is None else temp

    def __size(self, n: Node) -> int:
        if n is None:
            return 0
        return n.count

    def __rank(self, key: Any, n: Node) -> int:
        if n is None:
            return 0

        if key < n.key:
            return self.__rank(key, n.left)

        if key > n.key:
            return 1 + self.__size(n.left) + self.__rank(key, n.right)

        return self.__size(n.left)


if __name__ == '__main__':
    BST_ELEMENTS_QUANTITY = 3
    bst = BinarySearchTree()

    for i in range(BST_ELEMENTS_QUANTITY):
        bst.put(i, i + 1)

    for i in range(BST_ELEMENTS_QUANTITY):
        print(bst.get(i))
