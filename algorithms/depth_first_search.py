from data_structures.graph import Graph


def depth_first_search(graph: Graph, from_: int, to_: int):
    stack = []
    is_seen = {}

    stack.append(from_)

    while len(stack):
        to_see = stack.pop()

    return False

def depth_first_search_recursive(graph: Graph, from_: int, to_: int, is_seen=None) -> bool:
    if is_seen is None:
        is_seen = {}


    if from_ == to_:
        return True

    from_neighbours = graph.get_neighbours(from_)
    if from_neighbours is None:
        return

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

    oriented_graph = Graph(edges)
    oriented_graph.show_graph()
    print(f'{depth_first_search_recursive(oriented_graph, 1, 4) = }')  # must be True
    print(f'{depth_first_search_recursive(oriented_graph, 1, 6) = }')  # must be False

    print(f'{depth_first_search(oriented_graph, 1, 4) = }')  # must be True
    print(f'{depth_first_search(oriented_graph, 1, 6) = }')  # must be False
