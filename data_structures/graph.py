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

    def show_graph(self):
        print(self.__edges)


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

    g = Graph()
    g.add_edges(edges)
    g.show_graph()

    edges = [
        (1, 2),
        (1, 3),
        (1, 4),
    ]

    g = Graph()
    g.add_edges(edges, is_oriented=False)
    g.show_graph()

    print(g.get_neighbours(1))