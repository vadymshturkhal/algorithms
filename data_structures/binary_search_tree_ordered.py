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
        self.__count = 0
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

    def size(self):
        return self.__size(self.__root)

    def rank(self, key: Any) -> int:
        """How many keys < k?"""
        return self.__rank(key, self.__root)

    def min(self) -> Union[None, Node]:
        if self.__root is None:
            return None

        temp_node = self.__root
        while True:
            if temp_node.left is None:
                return temp_node
            temp_node = temp_node.left

    def max(self) -> Union[None, Node]:
        if self.__root is None:
            return None

        temp_node = self.__root
        while True:
            if temp_node.right is None:
                return temp_node
            temp_node = temp_node.right

    def floor(self, key: Any) -> Any:
        """Largest key ≤ a given key"""
        temp = self.__floor(self.__root, key)

        if temp is None:
            return None

        return temp.key

    def ceiling(self, key: Any) -> Any:
        """Smallest key ≥ a given key."""
        temp = self.__ceiling(self.__root, key)

        if temp is None:
            return None

        return temp.key

    def delete_min(self, node: Node = None) -> Union[None, Node]:
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
            prev_node = cursor_node
            cursor_node = cursor_node.left
            if cursor_node.left is None:
                prev_node.left = cursor_node.right
                break

        return cursor_node

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

            node_to_replace = self.delete_min(n.right)
            node_to_replace.left = n.left
            n = node_to_replace

        n.count = self.__size(n.left) + self.__size(n.right) + 1
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

    def __ceiling(self, n: Node, key: Any) -> Union[None, Node]:
        if n is None:
            return None

        if key == n.key:
            return n

        if key > n.key:
            return self.__ceiling(n.right, key)

        temp = self.__ceiling(n.left, key)

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

    print('original BST')
    print(*bst, '\n')

    bst.delete(3)
    print('After delete 3')
    print(*bst, '\n')

    print('After delete 5')
    bst.delete(5)
    print(*bst, '\n')

    print('min =', bst.min().key)
    print('After delete_min')
    bst.delete_min()
    print(*bst, '\n')
