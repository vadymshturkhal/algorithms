from typing import Union
from data_structures.node import Node
from data_structures.queue import Queue

class BST:
    def __init__(self):
        self.__root = None

    def insert(self, value) -> None:
        """Ignores same value"""

        if self.__root is None:
            self.__root = Node(value=value)
            return

        self.__insert(self.__root, value)

    def delete(self, value) -> None:
        if self.__root is None:
            return

        self.__root = self.__delete(self.__root, value)

    def delete_min(self, node=None) -> None:
        if self.__root is None:
            return
        
        if node is None:
            node = self.__root

        self.__root = self.__delete_min(node)

    def search_min(self, node=None) -> Union[None, Node]:
        if self.__root is None:
            return

        if node is None:
            node = self.__root
        
        if node.left is None:
            return node

        return self.search_min(node.left)

    def __insert(self, node, value):
        if node is None:
            return Node(value=value)

        if value > node.item:
            node.right = self.__insert(node.right, value)
        elif value < node.item:
            node.left = self.__insert(node.left, value)
        return node

    def __prepare_iterable(self, node, nodes: Queue):
        if node is None:
            return

        self.__prepare_iterable(node.left, nodes)
        nodes.enqueue(node.item)
        self.__prepare_iterable(node.right, nodes)

    def __delete_min(self, node):
        if node.left is None:
            """At the moment node has a minimum value"""
            self.__min = node
            return node.right

        node.left = self.__delete_min(node.left)
        return node

    def __delete(self, node, value):
        if node is None:
            return

        if value > node.item:
            node.right = self.__delete(node.right, value)
        elif value < node.item:
            node.left = self.__delete(node.left, value)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            self.delete_min(node.right)
            self.__min.left = node.left
            self.__min.right = node.right

            node.left = None
            node.right = None
            min = self.__min
            del self.__min
            return min
        return node

    def __iter__(self):
        self.__nodes = Queue()
        self.__prepare_iterable(self.__root, self.__nodes)
        return self

    def __next__(self):
        for value in self.__nodes:
            return value

        del self.__nodes
        raise StopIteration

if __name__ == '__main__':
    bst = BST()
    # nums_to_put = [12, 18, 15, 19, 13, 17, 5, 2, 9]
    nums_to_put = [5, 6, 7, 1, 4, -1, 5.5, 6.5]
    for num in nums_to_put:
        bst.insert(num)

    print(*bst)
    print(f'{bst.search_min().item = }')

    bst.delete_min() 
    print('\nAfter bst.delete_min()')
    print(*bst)

    bst.delete(6)
    print(*bst)

    bst.delete(7)
    print(*bst)

    bst.insert(1)
    bst.insert(1)
    bst.insert(1)
    print(*bst)
