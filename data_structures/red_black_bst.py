from typing import Union, Any
from data_structures.node import Node


class RedBlackBST:
    def __init__(self):
        self.__RED = True
        self.__BLACK = False
        self.__root = None

    def get(self, key) -> Union[None, Any]:
        """Search is the same as for elementary BST (ignore color)"""
        current_node = self.__root

        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return current_node.item

        return None

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
        temp.color = n.color
        temp.right = n
        n.color = self.__RED
        return temp

    def __flip_colors(self, n: Node) -> None:
        n.color = self.__RED
        n.left.color = self.__BLACK
        n.right.color = self.__BLACK


if __name__ == '__main__':
    rb = RedBlackBST()
