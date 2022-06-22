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

    def search(self, key, also_return_parent=False):
        current_node = self.__root
        parent = None
        while current_node is not None and key != current_node.key:
            parent = current_node

            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if also_return_parent:
            return current_node, parent

        return current_node

    def delete_key(self, key):
        node_to_del, parent = self.search(key, also_return_parent=True)

        # Node with the key doesn't exist
        if node_to_del is None:
            return

    def min_key(self, node=None, return_node=False):
        if node is None:
            node = self.__root

        key = None

        while node is not None:
            key = node.key
            node = node.left

        return key if not return_node else node

    def max_key(self, node=None, return_node=False):
        if node is None:
            node = self.__root

        node = self.__root
        key = None

        while node is not None:
            key = node.key
            node = node.right

        return key if not return_node else node

    def successor_key(self, key, return_node=False):
        """Returns node with the smallest key bigger than given"""

        node = self.search(key)

        if node is None:
            return

        if node.right is not None:
            return self.min_key(node.right, return_node)
        return

    def predecessor_key(self, key, return_node=False):
        """Returns node with the biggest key smaller than given"""
        node = self.search(key)

        if node is None:
            return

        if node.left is not None:
            return self.max_key(node.left, return_node)
        return

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
    nums_to_put = [15, 6, 3, 2, 4, 7, 13, 9, 18, 20, 17]
    for num in nums_to_put:
        bst.insert(num)

    print(*bst)
    print(f'{bst.min_key() = }')
    print(f'{bst.max_key() = }')

    bst.delete_key(2)
    print(*bst)
