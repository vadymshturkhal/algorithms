from typing import Union, Any
from data_structures.node import Node
from data_structures.queue import Queue


class RedBlackBST:
    def __init__(self):
        self.__root = None
        self.__RED = True
        self.__BLACK = False

    def insert(self, value) -> None:
        """Ignores same value"""
        self.__root = self.__insert(self.__root, value)

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

    def __insert(self, node, value):
        if node is None:
            return Node(value=value, color=self.__RED)

        if value > node.item:
            node.right = self.__insert(node.right, value)
        elif value < node.item:
            node.left = self.__insert(node.left, value)
        else:  # Ignore when the same
            pass

        if self.__is_red(node.right) and not self.__is_red(node.left):
            node = self.__rotate_left(node)

        if self.__is_red(node.left) and self.__is_red(node.left.left):
            node = self.__rotate_right(node)

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

    def __prepare_iterable(self, node, nodes: Queue):
        if node is None:
            return

        self.__prepare_iterable(node.left, nodes)
        nodes.enqueue(node.item)
        self.__prepare_iterable(node.right, nodes)

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
    rb_bst = RedBlackBST()
    # to_put = [12, 18, 15, 19, 13, 17, 5, 2, 9]
    # nums_to_put = [5, 6, 7, 1, 4, -1, 5.5, 6.5]
    # to_put = ['a', 'b']
    to_put = ['s', 'e', 'a', 'r', 'c', 'h', 'x', 'm', 'p', 'l']

    for num in to_put:
        rb_bst.insert(num)

    print(*rb_bst)
