from data_structures.graph import Graph
from algorithms.graph_topological_sort import topological_sort

def reverse_graph(graph):
    pass


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
        (11, 12),
        (12, 9),
    ]

    graph = Graph(edges, is_directed=True)
    topological_order = topological_sort(graph)
    print(topological_order)
