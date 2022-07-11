from data_structures.graph import Graph


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
