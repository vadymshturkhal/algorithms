from copy import deepcopy


class Graph:
    """
        Used dict.
    """

    def __init__(self, edges: list = None, *, is_directed=True) -> None:
        self.__is_directed = is_directed
        self.__vertices = {}
        self.__edges = {}
        self.add_edges(edges)

    @property
    def is_directed(self):
        return self.__is_directed

    def add_edges(self, edges: list = None) -> None:
        """
            Edges must be unique.
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

            vertex, neighbours = edge
    
            is_compact_neighbours = type(neighbours) == list

            if is_compact_neighbours:
                for neighbour in neighbours:
                    self.add_edge((vertex, neighbour))
                continue

            self.add_edge((vertex, neighbours))

    def add_edge(self, edge, *, data=None):
        from_, to_ = edge
        self.__guarantee_vertex(from_)
        self.add_vertex(from_)

        self.__edges[from_][to_]= data
        self.add_vertex(to_)

        if not self.is_directed:
            self.__guarantee_vertex(to_)
            self.__edges[to_][from_]= self.__edges[to_].get(from_)

    def add_vertex(self, vertex, *, value=None):
        if vertex in self.__vertices:
            return
        self.__vertices[vertex] = value

    def get_vertex(self, vertex_key):
        if vertex_key in self.__vertices:
            return deepcopy(self.__vertices[vertex_key])

    def get_all_vertices(self):
        return deepcopy(list(self.__vertices.keys()))

    def update_vertex_value(self, vertex_key, new_vertex_value):
        if vertex_key in self.__vertices:
            self.__vertices[vertex_key] = new_vertex_value
    
    def is_vertex_exist(self, vertex_id):
        return vertex_id in self.__vertices

    def get_neighbours(self, vertex: int) -> list:
        """Returned copy of vertices"""
        if vertex not in self.__edges:
            return []

        return list(self.__edges[vertex])

    def is_edge_exist(self, from_: int, to_: int) -> bool:
        if from_ in self.__edges:
            if to_ in self.__edges[from_]:
                return True
        return False

    def get_edge_value(self, edge):
        if len(edge) != 2:
            return

        a, b = edge
        if a in self.__edges:
            return deepcopy(self.__edges[a].get(b))

    def get_all_edges(self):
        all_edges = []
        for start_vertex, end_vertices in self.__edges.items():
            end_vertices = list(end_vertices.keys())
            for end_vertex in end_vertices:
                all_edges.append((start_vertex, end_vertex))

        return all_edges

    def update_edge_value(self, edge, new_value):
        if len(edge) != 2:
            return
        
        a, b = edge
        if a in self.__edges:
            if b in self.__edges[a]:
                self.__edges[a][b] = new_value

    def show_graph(self):
        for key, value in self.__edges.items():
            print(key, '->', list(value))

    def __guarantee_vertex(self, vertex):
        if vertex not in self.__edges:
            self.__edges[vertex] = {}

    def __repr__(self):
        return 'Graph'


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
    print(f'{oriented_graph.is_directed = }')
    oriented_graph.show_graph()

    edges = [
        (1, [2, 3]),
        (3, [2, 4]),
        (5, [4]),
        (6, 5)
    ]

    graph = Graph(is_directed=False)
    graph.add_edges(edges)
    print(f'{graph.is_directed = }')
    graph.show_graph()
    print()
    print(f'{graph.get_neighbours(1) = }')
    print(f'{graph.get_neighbours(10) = }')
    print(f'{graph.is_edge_exist(1, 4) = }')
    print(f'{graph.is_edge_exist(1, 10) = }')
    print(f'{graph.is_edge_exist(1, 2) = }')
    print(f'{graph.get_vertex(1) = }')
    graph.update_vertex_value(1, ['a', 'b'])
    print("After graph.update_vertex_value(1, ['a', 'b'])")
    print(f'{graph.get_vertex(1) = }')
