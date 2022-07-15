from data_structures.graph import Graph


def dijkstra_shortest_path(oriented_graph, start_vertex):
    pass


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

    dir_graph.show_graph()
