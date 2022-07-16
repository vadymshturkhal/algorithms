from data_structures.graph import Graph
from math import inf
from data_structures.binary_heap import BinaryHeap


def dijkstra_shortest_path(directed_graph: Graph, start_vertex) -> Graph:
    if not directed_graph.is_vertex_exist(start_vertex):
        return

    binary_heap = BinaryHeap(comparator=edge_weight_comparator)
    neighbour_edges = {}
    is_seen = {}

    shortest_path_graph = init_all_vertices_with_inf_weight(directed_graph, start_vertex)

    start_vertex = (start_vertex, 0)
    binary_heap.insert(start_vertex)
    while len(binary_heap):
        to_see, to_see_weight = binary_heap.del_element()

        is_seen[to_see] = True

        for neighbour in directed_graph.get_neighbours(to_see):
            if neighbour in is_seen:
                continue

            edge = (to_see, neighbour)
            edge_weight = directed_graph.get_edge_value(edge)['weight']

            neighbour_weight = shortest_path_graph.get_vertex(neighbour)['weight']
            current_path_weight_to_neighbour = to_see_weight + edge_weight

            if current_path_weight_to_neighbour < neighbour_weight:
                shortest_path_graph.update_vertex_value(neighbour, {'weight': current_path_weight_to_neighbour})
                neighbour_edges[neighbour] = edge

                to_insert = (neighbour, current_path_weight_to_neighbour)
                binary_heap.insert(to_insert)

    for edge in neighbour_edges.values():
        shortest_path_graph.add_edge(edge, data=directed_graph.get_edge_value(edge))

    return shortest_path_graph

def edge_weight_comparator(first_vertex, second_vertex):
    first_vertex, first_weigth = first_vertex
    second_vertex, second_weight = second_vertex

    if first_weigth < second_weight:
        returned_value = -1
    elif first_weigth > second_weight:
        returned_value = 1
    else:
        returned_value = 0
    
    return returned_value

def init_all_vertices_with_inf_weight(graph: Graph, source_vertex) -> Graph:
    shortest_path_graph = Graph()

    for vertex in graph.get_all_vertices():
        shortest_path_graph.add_vertex(vertex)
        if vertex == source_vertex:
            shortest_path_graph.update_vertex_value(vertex, {'weight': 0})
            continue

        shortest_path_graph.update_vertex_value(vertex, {'weight': inf})

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

    for vertex in shortest_graph.get_all_vertices():
        print(vertex, shortest_graph.get_vertex(vertex))

    for edge in shortest_graph.get_all_edges():
        print(edge, shortest_graph.get_edge_value(edge))
