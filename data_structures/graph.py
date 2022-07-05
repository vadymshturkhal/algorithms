class Graph:
    """
        Used dict.
    """

    def __init__(self, edges: list = None) -> None:
        self.__edges = {}
        self.add_edges(edges)

    def add_edges(self, edges: list = None, *, is_oriented: bool = True) -> None:
        """
            Edges might be both 
                [(1, 2), (1, 3)]
                [(1, [2, 3, 4])]

        """
        if edges is None:
            return
        if len(edges) < 1:
            return

        for edge in edges:
            if len(edge) != 2:
                raise StopIteration(f'Can\'t parse the edge {edge}')

            from_, to_ = edge
            self.__guarantee_vertex(from_)

            is_compact_neighbours = type(to_) == list

            if is_compact_neighbours:
                for neighbour in to_:
                    self.__edges[from_][neighbour]= None
                
                    if not is_oriented:
                        self.__guarantee_vertex(neighbour)
                        self.__edges[neighbour][from_]= None
                continue

            self.__edges[from_][to_]= None

            if not is_oriented:
                self.__guarantee_vertex(to_)
                self.__edges[to_][from_]= None

    def get_neighbours(self, vertex: int) -> list:
        """Returned copy of vertecies"""
        if vertex not in self.__edges:
            return []

        return list(self.__edges[vertex])

    def is_edge_exist(self, from_: int, to_: int) -> bool:
        if from_ in self.__edges:
            if to_ in self.__edges[from_]:
                return True
        return False

    def show_graph(self):
        for key, value in self.__edges.items():
            print(key, '->', list(value))

    def __guarantee_vertex(self, vertex):
        if vertex not in self.__edges:
            self.__edges[vertex] = {}


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
        (1, [2, 3]),
        (3, [2, 4]),
        (5, [4]),
        (6, 5)
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
