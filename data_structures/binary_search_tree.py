from typing import Any, Union
from data_structures.node import Node


class BinarySearchTree:
    """
        Symmetric order.
        Each node has a key, and every node’s key is:
            1. Larger than all keys in its left subtree;
            2.Smaller than all keys in its right subtree.
    """

    def __init__(self):
        self.__root = None

    def put(self, item: Any) -> None:
        pass

    def get(self) -> Union[None, Any]:
        pass

    def delete(self) -> None:
        pass
