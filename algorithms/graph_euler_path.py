from data_structures.graph import Graph


def euler_path(graph: Graph, start_vertex: int) -> list:
    stack = []
    euler_path_sequence = []

    vertices = {}

    stack.append(start_vertex)

    while len(stack):
        top_vertex = stack[-1]

        if top_vertex not in vertices:
            vertices[top_vertex] = graph.get_neighbours(top_vertex)

        neighbours = vertices[top_vertex]

        if len(neighbours):
            first_neighbour = neighbours[0]

            if first_neighbour not in vertices:
                vertices[first_neighbour] = graph.get_neighbours(first_neighbour)

            vertices[first_neighbour].remove(top_vertex)
            vertices[top_vertex].remove(first_neighbour)

            stack.append(first_neighbour)
        else:
            euler_path_sequence.append(stack.pop())

    return euler_path_sequence


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

    graph = Graph(edges, is_oriented=False)
    # or_graph = Graph(edges)
    # graph.show_graph()
    # print()
    # or_graph.show_graph()
    # print()

    print(f'{euler_path(graph, 1) = }')
    # print()
    # print(f'{euler_path(or_graph, 1) = }')
