from data_structures.graph import Graph


def get_connected_components(graph: Graph) -> list:
    """Returns list of connected components"""
    stack = []
    is_seen = {}
    all_components = []

    for vertex in graph.get_all_vertices():
        if vertex in is_seen:
            continue

        current_component = []
        stack.append(vertex)

        while len(stack):
            to_see = stack[-1]

            if to_see not in is_seen:
                is_seen[to_see] = graph.get_neighbours(to_see)

            if len(is_seen[to_see]):
                # Get last but not first element of neighbours, for efficiency
                to_watch = is_seen[to_see].pop()

                if to_watch not in is_seen:
                    stack.append(to_watch)
            else:
                seen_vertex = stack.pop()
                current_component.append(seen_vertex)

        all_components.append(current_component)

    return all_components


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

        (15, 16),
        (16, 19),

        (102, 103),
    ]

    graph = Graph(edges, is_directed=False)
    # graph.show_graph()
    # print()

    connected_components = get_connected_components(graph)
    print(f'{len(connected_components) = }')  # must be 3
