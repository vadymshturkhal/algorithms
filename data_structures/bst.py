from typing_extensions import Self
from data_structures.node import Node

class BST:
    def __init__(self) -> None:
        self.__root = None

    def insert(self, value) -> None:
        new_node = Node(value=value)

        if self.__root is None:
            self.__root = new_node
            return
        
        current_node = self.__root
        while True:
            if value > current_node.item:
                if current_node.right is None:
                    current_node.right = new_node
                    break
                else:
                    current_node = current_node.right
            else:
                if current_node.left is None:
                    current_node.left = new_node
                    break
                else:
                    current_node = current_node.left

    def delete(self, value) -> None:
        pass

    def print_values(self) -> None:
        self.__print(self.__root)

    def __print(self, node):
        if node is None:
            return

        self.__print(node.left)
        print(node.item)
        self.__print(node.right)

if __name__ == '__main__':
    bst = BST()
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(1)
    bst.insert(4)
    bst.insert(-1)

    bst.print_values()
