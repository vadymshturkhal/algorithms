from data_structures.graph import Graph


def connected_components(graph: Graph) -> int:
    stack = []
    is_seen = {}
    components = 0

    for vertex in graph.get_all_vertices():
        if vertex in is_seen:
            continue

        components += 1
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
                stack.pop()

    return components

def begin():
    pass


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

    graph = Graph(edges, is_oriented=False)
    graph.show_graph()
    print()

    connected_components_quantity = connected_components(graph)
    print(f'{connected_components_quantity = }')
