from typing import Union
from data_structures.node import Node
from data_structures.queue import Queue

class BST:
    def __init__(self):
        self.__root = None

if __name__ == '__main__':
    bst = BST()
    nums_to_put = [5, 6, 7, 1, 4, -1, 5.5, 6.5]
    for num in nums_to_put:
        bst.insert(num)
