from data_structures.graph import Graph
from algorithms.graph_topological_sort import topological_sort
from graph_connected_components import get_connected_components
from graph_reverse import reverse_graph


def get_strongly_connected_components(graph: Graph) -> list:
    reversed_graph = reverse_graph(graph)
    topological_order = topological_sort(reversed_graph, is_classic_order=False)
    topological_order.reverse()

    return get_connected_components(graph, topological_order)



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

    graph = Graph(edges, is_directed=True)
    # graph.show_graph()
    # print()

    strongly_connected_components = get_strongly_connected_components(graph)
    print(strongly_connected_components)
    print(len(strongly_connected_components))  # must be 5
