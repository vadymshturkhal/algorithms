from data_structures.graph import Graph
from data_structures.binary_heap import BinaryHeap


def get_min_spanning_tree(graph: Graph) -> Graph:
    min_span_tree = Graph()

    weight_binary_heap = create_weight_binary_heap_with(graph)

    for edge in weight_binary_heap:
        print(edge)

    return min_span_tree

def create_weight_binary_heap_with(graph: Graph):
    all_edges = graph.get_all_edges()

    def edge_weight_comparator(first_edge, second_edge):
        first_edge, first_weigth = first_edge
        second_edge, second_weight = second_edge

        if first_weigth < second_weight:
            returned_value = -1
        elif first_weigth > second_weight:
            returned_value = 1
        else:
            returned_value = 0
        
        return returned_value
    
    binary_heap = BinaryHeap(comparator=edge_weight_comparator)

    for edge in all_edges:
        edge_to_compare = [edge, graph.get_edge_value(edge)['weight']]
        binary_heap.insert(edge_to_compare)

    return binary_heap


if __name__ == '__main__':
    edges = [
        [(0, 7), {'weight': 0.16}],
        [(2, 3), {'weight': 0.17}],
        [(1, 7), {'weight': 0.19}],
        [(0, 2), {'weight': 0.26}],
        [(5, 7), {'weight': 0.28}],
        [(1, 3), {'weight': 0.29}],
        [(1, 5), {'weight': 0.32}],
        [(2, 7), {'weight': 0.34}],
        [(4, 5), {'weight': 0.35}],
        [(1, 2), {'weight': 0.36}],
        [(4, 7), {'weight': 0.37}],
        [(0, 4), {'weight': 0.38}],
        [(6, 2), {'weight': 0.40}],
        [(3, 6), {'weight': 0.52}],
        [(6, 0), {'weight': 0.58}],
        [(6, 4), {'weight': 0.93}],
    ]

    dir_graph = Graph(is_directed=True)

    for edge in edges:
        vertices, data = edge
        dir_graph.add_edge(vertices, data=data)

    # dir_graph.show_graph()
    # print()

    min_span_tree = get_min_spanning_tree(dir_graph)
    min_span_tree.show_graph()