from data_structures.graph import Graph


def get_min_spanning_tree(graph: Graph) -> Graph:
    min_span_tree = Graph()
    return min_span_tree


if __name__ == '__main__':
    edges = [
        (0, [1, 5]),
        (2, [0, 3]),
        (3, [5, 2]),
        (4, [2, 3]),
        (5, 4),
        (6, [0, 4, 8, 9]),
        (7, [6, 9]),
        (8, 6),
        (9, [10, 11]),
        (10, 12),
        (11, [12, 4]),
        (12, 9),
    ]

    dir_graph = Graph(edges, is_directed=True)
    dir_graph.show_graph()
    print()

    min_span_tree = get_min_spanning_tree(dir_graph)
    min_span_tree.show_graph()
