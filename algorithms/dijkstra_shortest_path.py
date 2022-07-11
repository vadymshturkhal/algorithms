from data_structures.graph import Graph


def dijkstra_shortest_path(graph):
    pass


if __name__ == '__main__':
    edges = [
        (1, 2),
        (2, [3, 4, 6]),
        (3, 6),
        (4, [3, 5]),
        (5, 4),
        (6, 5),
    ]

    or_graph = Graph(edges)
    or_graph.show_graph()

    x = or_graph.get_edge_value((1, 2))
    print(x)