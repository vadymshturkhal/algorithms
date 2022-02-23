from typing import Any, Union
from data_structures.node import Node


class BinarySearchTree:
    """
        Symmetric order.
        Each node has a key, and every node’s key is:
            1. Larger than all keys in its left subtree;
            2. Smaller than all keys in its right subtree.
    """

    def __init__(self):
        self.__root = None

    def put(self, key: Any, item: Any) -> None:
        pass

    def __put(self, node: Node, key: Any, item: Any) -> Node:
        if node is None:
            return Node(key, item)

        if key < node.key:
            node.previous = self.__put(node.previous, key, item)
        elif key > node.key:
            node.next_node = self.__put(node.next_node, key, item)
        else:
            node.item = item

        return node

    def get(self, key) -> Union[None, Any]:
        current_node = self.__root

        while current_node is not None:
            if current_node.key < key:
                current_node = current_node.previous
            elif current_node.key > key:
                current_node = current_node.next_node
            else:
                return current_node.item

        return None

    def delete(self) -> None:
        pass
