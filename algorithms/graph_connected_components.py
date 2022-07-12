from data_structures.graph import Graph


def connected_components(graph: Graph) -> int:
    pass


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

    or_graph = Graph(edges)
    or_graph.show_graph()
    print()
    connected_components_quntity = connected_components(or_graph)
    print(f'{connected_components_quntity = }')
