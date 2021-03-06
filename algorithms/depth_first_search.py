from data_structures.graph import Graph


def depth_first_search(graph: Graph, from_: int, to_: int) -> bool:
    stack = []
    is_seen = {}

    stack.append(from_)

    while len(stack):
        to_see = stack[-1]

        if to_see not in is_seen:
            is_seen[to_see] = graph.get_neighbours(to_see)

        if len(is_seen[to_see]):
            # Get last but not first element of neighbours, for efficiency
            to_watch = is_seen[to_see].pop()

            if to_watch not in is_seen:
                if to_watch == to_:
                    return True

                stack.append(to_watch)
        else:
            stack.pop()

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
        (1, [2, 4, 12]),
        (2, 4),
        (12, [4, 10, 11]),
        (10, 11),
        (4, [6, 7]),
        (7, [3, 6]),
        (6, [5, 9, 13]),
        (5, [8, 9]),
        (8, 9),
    ]

    graph = Graph(edges, is_directed=False)
    # graph.show_graph()
    # print()

    print(f'{depth_first_search_recursive(graph, 1, 9) = }')  # must be True
    print(f'{depth_first_search_recursive(graph, 1, 16) = }')  # must be False

    d_graph = Graph(edges)
    # d_graph.show_graph()
    # print()
    # print(f'{depth_first_search(d_graph, 1, 9) = }')  # must be True
    # print(f'{depth_first_search(d_graph, 1, 16) = }')  # must be False
