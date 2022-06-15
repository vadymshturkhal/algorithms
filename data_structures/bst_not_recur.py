from data_structures.node import Node
from data_structures.queue import Queue

class BST:
    def __init__(self):
        self.__root = None

    def insert(self, key, value=None):
        node = Node(key, value)
        if self.__root is None:
            self.__root = node
            return

        parent = None
        cursor = self.__root

        while cursor is not None:
            parent = cursor
            if key < cursor.key:
                cursor = cursor.left
            else:
                cursor = cursor.right
        
        if key < parent.key:
            parent.left = node
        else:
            parent.right = node

    def search(self, key):
        current_node = self.__root
        while current_node is not None and key != current_node.key:
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return current_node

    def min_key(self, node=None):
        if node is None:
            node = self.__root

        key = None

        while node is not None:
            key = node.key
            node = node.left

        return key

    def max_key(self, node=None):
        if node is None:
            node = self.__root

        node = self.__root
        key = None

        while node is not None:
            key = node.key
            node = node.right

        return key

    def __prepare_iterable(self, node, nodes: Queue):
        if node is None:
            return

        self.__prepare_iterable(node.left, nodes)
        nodes.enqueue(node.key)
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
    bst = BST()
    nums_to_put = [5, 6, 7, 1, 4, -1, 5.5, 6.5]
    for num in nums_to_put:
        bst.insert(num)

    print(bst.min_key())
    print(bst.max_key())
    print(*bst)
