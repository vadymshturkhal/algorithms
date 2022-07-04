from data_structures.graph import Graph

def depth_first_search(graph: Graph, from_, to_):
    return False


if __name__ == '__main__':
    edges = [
        (1, 2),
        (1, 3),
        (3, 2),
        (3, 4),
        (5, 4),
        (5, 6),
        (6, 5)
    ]

    g = Graph()
    g.add_edges(edges)
    g.show_graph()

    is_path_exist = depth_first_search(g, 1, 4)  # must be True
    print(is_path_exist)
