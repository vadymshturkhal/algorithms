class Graph:
    """
        Used incidence list.
        Edge is list with tuples with ints.
    """

    def __init__(self, edges: list = None) -> None:
        self.__edges = self.add_edges(edges)

    def add_edges(self, edges: list = None, *, is_oriented: bool = True) -> None:
        if edges is None:
            edges = []
            return edges

        for edge in edges:
            from_, to_ = edge

            self.__init_len_of_edges(from_)
            self.__edges[from_].append(to_)

            if not is_oriented:
                self.__init_len_of_edges(to_)
                self.__edges[to_].append(from_)

    def show_graph(self):
        print(self.__edges)

    def __init_len_of_edges(self, required_len: int):
        while required_len >= len(self.__edges):
            self.__edges.append([])


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
