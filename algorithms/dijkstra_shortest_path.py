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

    weights = [
        ((1, 2), 1),
        ((2, 3), 5),
        ((2, 4), 2),
        ((2, 6), 7),
        ((3, 6), 1),
        ((4, 3), 1),
        ((4, 5), 4),
        ((5, 4), 3),
        ((6, 5), 1),
    ]

    for edge, weight in weights:
        or_graph.update_edge_value(edge, {'weight': weight})

    or_graph.show_graph()
