from data_structures.graph import Graph
from algorithms.graph_topological_sort import topological_sort


def reverse_graph(graph: Graph):
    reversed_edges = reverse_edges(graph)
    parsed_edges = parse_edges(reversed_edges)
    print(parsed_edges)

def reverse_edges(graph: Graph) -> dict:
    all_vertices = graph.get_all_vertices()
    reversed_edges = {}

    for vertex in all_vertices:
        vertex_neighbours = graph.get_neighbours(vertex)
        for neighbour in vertex_neighbours:
            if neighbour not in reversed_edges:
                reversed_edges[neighbour] = []
            reversed_edges[neighbour].append(vertex)

    return reversed_edges

def parse_edges(vertices: dict) -> list:
    edges = []
    for vertex, neighbours in vertices.items():
        edges.append((vertex, neighbours))
    return edges


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
    reverser_graph = reverse_graph(graph)

    # topological_order = topological_sort(graph)
    # print(topological_order)
