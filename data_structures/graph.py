class Graph:
    """
        Used dict.
    """

    def __init__(self, edges: list = None) -> None:
        self.__edges = {}
        self.add_edges(edges)

    def add_edges(self, edges: list = None, *, is_oriented: bool = True) -> None:
        if edges is None:
            return

        for edge in edges:
            from_, to_ = edge

            if from_ not in self.__edges:
                self.__edges[from_] = {}

            self.__edges[from_][to_]= None

            if not is_oriented:
                if to_ not in self.__edges:
                    self.__edges[to_] = {}
                self.__edges[to_][from_]= None

    def get_neighbours(self, vertex: int) -> list:
        """Returned copy of vertecies"""
        if vertex not in self.__edges:
            return

        return list(self.__edges[vertex])

    def is_edge_exist(self, from_: int, to_: int) -> bool:
        if from_ in self.__edges:
            if to_ in self.__edges[from_]:
                return True
        return False

    def show_graph(self):
        for key, value in self.__edges.items():
            print(key, '->', list(value))


if __name__ == '__main__':
    edges = [
        (1, 2),
        (1, 3),
        (3, 2),
        (3, 4),
        (5, 4),
        (5, 6),
        (6, 5)
    ]

    oriented_graph = Graph()
    oriented_graph.add_edges(edges)
    print('Oriented graph')
    oriented_graph.show_graph()
    print()

    edges = [
        (1, 2),
        (1, 3),
        (1, 4),
    ]

    graph = Graph()
    graph.add_edges(edges, is_oriented=False)
    print('Graph')
    graph.show_graph()
    print()
    print(f'{graph.get_neighbours(1) = }')
    print(f'{graph.get_neighbours(10) = }')
    print(f'{graph.is_edge_exist(1, 4) = }')
    print(f'{graph.is_edge_exist(1, 10) = }')
