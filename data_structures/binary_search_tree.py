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

    def delete(self) -> None:
        pass

    def delete_min(self) -> None:
        cursor_node = self.__root
        if cursor_node is None:
            return None

        if cursor_node.left is None:
            self.__root = self.__root.right
            return None

        while True:
            prev_node = cursor_node
            cursor_node = cursor_node.left
            if cursor_node.left is None:
                prev_node.left = cursor_node.right
                break

        return None

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


if __name__ == '__main__':
    BST_ELEMENTS_QUANTITY = 3
    bst = BinarySearchTree()

    for i in range(BST_ELEMENTS_QUANTITY):
        bst.put(i, i + 1)

    for i in range(BST_ELEMENTS_QUANTITY):
        print(bst.get(i))

    print('After delete_min')
    bst.delete_min()
    for i in range(BST_ELEMENTS_QUANTITY):
        print(bst.get(i))
