from data_structures.graph import Graph


def breadth_first_search(graph: Graph, from_: int, to_: int) -> bool:
    return False


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
    graph.show_graph()

    print()
    print(f'{breadth_first_search(graph, 1, 9) = }')  # must be True
    print(f'{breadth_first_search(graph, 1, 16) = }')  # must be False

    print(f'{breadth_first_search(graph, 1, 9) = }')  # must be True
    print(f'{breadth_first_search(graph, 1, 16) = }')  # must be False
