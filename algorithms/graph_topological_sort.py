from data_structures.graph import Graph


def topological_sort(graph: Graph) -> list:
    """Returns vertices in topological sort"""
    stack = []
    is_seen = {}
    topological = []

    for vertex in sorted(graph.get_all_vertices()):
        if vertex in is_seen:
            continue

        stack.append(vertex)

        while len(stack):
            to_see = stack[-1]

            if to_see not in is_seen:
                is_seen[to_see] = sorted(graph.get_neighbours(to_see), reverse=True)

            if len(is_seen[to_see]):
                # Get last but not first element of neighbours, for efficiency
                to_watch = is_seen[to_see].pop()

                if to_watch not in is_seen:
                    stack.append(to_watch)
            else:
                seen_vertex = stack.pop()
                topological.append(seen_vertex)

    return topological


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

    edges = [
        (0, [1, 5, 2]),
        (3, [5, 6, 4, 2]),
        (5, 2),
        (6, [0, 4]),
        (1, 4),
    ]

    graph = Graph(edges, is_directed=True)
    topological_order = topological_sort(graph)
    print(topological_order == [4, 1, 2, 5, 0, 6, 3])
