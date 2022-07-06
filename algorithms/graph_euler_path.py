from data_structures.graph import Graph


def euler_path(graph: Graph, start_vertex: int) -> list:
    euler_path_sequence = []
    return euler_path_sequence


if __name__ == '__main__':
    edges = [
        (1, [2, 4, 12]),
        (2, 4),
        (12, [4, 10, 11]),
        (10, 11),
        (4, [6, 7]),
        (7, [3, 6]),
        (6, [5, 9, 13]),
        (5, [8, 9]),
        (8, 9),
    ]

    graph = Graph(edges, is_oriented=False)
    # or_graph = Graph(edges)
    # graph.show_graph()
    # print()
    # or_graph.show_graph()
    # print()

    print(f'{euler_path(graph, 1) = }')
    # print()
    # print(f'{euler_path(or_graph, 1) = }')
