from typing import Any


class Node:
    """Node for data structures"""

    def __init__(self):
        self.item = None
        self.forward = None
        self.previous = None

    def add_item(self, item: Any) -> None:
        pass

    def add_next(self, n: 'Node') -> None:
        pass
