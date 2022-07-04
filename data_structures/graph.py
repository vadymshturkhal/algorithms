from node import Node


class Graph:
    """Edge is list with tuples with ints"""

    def __init__(self, edges=None) -> None:
        self.__edges = self.add_edges(edges)

    def add_edges(self, edges: None) -> None:
        if edges is None:
            edges = []
            return edges
        
        for edge in edges:
            from_, to_ = edge

            while from_ >= len(self.__edges):
                self.__edges.append([])

            self.__edges[from_].append(to_)

    def show_graph(self):
        print(self.__edges)


if __name__ == '__main__':
    NODES_QUANTITY = 10
    g = Graph()

    edges = [
        (1, 2),
        (1, 3),
        (3, 2),
        (3, 4),
        (5, 4),
        (5, 6),
        (6, 5)
    ]

    g.add_edges(edges)
    g.show_graph()

