from data_structures.graph import Graph

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
