from data_structures.graph import Graph
from queue import SimpleQueue
from math import inf


def dijkstra_shortest_path(directed_graph: Graph, start_vertex) -> Graph:
    queue_ = SimpleQueue()
    shortest_path_graph = Graph()
    neighbour_edges = {}
    is_seen = {}

    if not directed_graph.is_vertex_exist(start_vertex):
        return

    if directed_graph.get_vertex(start_vertex) is None:
        directed_graph.update_vertex_value(start_vertex, {'weight': 0})

    queue_.put(start_vertex)
    while not queue_.empty() :
        to_see = queue_.get()
        is_seen[to_see] = True

        for neigbour in directed_graph.get_neighbours(to_see):
            if neigbour in is_seen:
                continue

            queue_.put(neigbour)

            edge = (to_see, neigbour)
            edge_weight = directed_graph.get_edge_value(edge)['weight']

            if directed_graph.get_vertex(neigbour) is None:
                directed_graph.update_vertex_value(neigbour, {'weight': inf})

            to_see_weight = directed_graph.get_vertex(to_see)['weight']
            neighbour_weight = directed_graph.get_vertex(neigbour)['weight']
            current_path_weight_to_neighbour = to_see_weight + edge_weight

            if current_path_weight_to_neighbour < neighbour_weight:
                directed_graph.update_vertex_value(neigbour, {'weight': current_path_weight_to_neighbour})
                neighbour_edges[neigbour] = edge

    for edge in neighbour_edges.values():
        shortest_path_graph.add_edge(edge, data=directed_graph.get_edge_value(edge))
    
    return shortest_path_graph


if __name__ == '__main__':
    edges = [
        [(0, 1), {'weight': 5}],
        [(0, 4), {'weight': 9}],
        [(0, 7), {'weight': 8}],
        [(1, 2), {'weight': 12}],
        [(1, 3), {'weight': 15}],
        [(1, 7), {'weight': 4}],
        [(2, 3), {'weight': 3}],
        [(2, 6), {'weight': 11}],
        [(3, 6), {'weight': 9}],
        [(4, 5), {'weight': 4}],
        [(4, 6), {'weight': 20}],
        [(4, 7), {'weight': 5}],
        [(5, 2), {'weight': 1}],
        [(5, 6), {'weight': 13}],
        [(7, 5), {'weight': 6}],
        [(7, 2), {'weight': 7}],
    ]

    dir_graph = Graph(is_directed=True)

    for edge in edges:
        vertices, data = edge
        dir_graph.add_edge(vertices, data=data)

    shortest_graph = dijkstra_shortest_path(dir_graph, 0)
    shortest_graph.show_graph()
