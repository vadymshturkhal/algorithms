from data_structures.graph import Graph

def depth_first_search_recursive(graph: Graph, from_: int, to_: int, is_seen=None) -> bool:
    if is_seen is None:
        is_seen = {}

    if from_ == to_:
        return True

    from_neighbours = graph.get_neighbours(from_)
    is_seen[from_] = is_seen.get(from_, True)

    for neigbour in from_neighbours:
        if is_seen.get(neigbour) is None:
            is_found = depth_first_search_recursive(graph, neigbour, to_, is_seen)
            if is_found:
                return True

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

    g = Graph(edges)
    is_path_exist = depth_first_search_recursive(g, 1, 4)  # must be True
    print(is_path_exist)

    is_path_exist = depth_first_search_recursive(g, 1, 6)  # must be False
    print(is_path_exist)
