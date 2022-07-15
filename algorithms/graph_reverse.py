from data_structures.graph import Graph


def reverse_graph(graph: Graph):
    reversed_edges = reverse_edges(graph)
    parsed_edges = parse_edges(reversed_edges)
    reversed_graph = Graph(parsed_edges, is_directed=True)
    return reversed_graph

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
