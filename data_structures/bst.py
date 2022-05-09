from data_structures.node import Node
from data_structures.queue import Queue

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
    
    def __iter__(self):
        self.__nodes = Queue()
        self.__prepare_iterable(self.__root, self.__nodes)
        return self

    def __prepare_iterable(self, node, nodes: Queue):
        if node is None:
            return

        self.__prepare_iterable(node.left, nodes)
        nodes.enqueue(node.item)
        self.__prepare_iterable(node.right, nodes)

    def __next__(self):
        for value in self.__nodes:
            return value
        
        del self.__nodes
        raise StopIteration

if __name__ == '__main__':
    bst = BST()
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(1)
    bst.insert(4)
    bst.insert(-1)
    bst.insert(-1)

    print(*bst)
