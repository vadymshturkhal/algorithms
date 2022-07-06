from data_structures.graph import Graph
from queue import SimpleQueue


def graph_frame_breadth_first_search(graph: Graph, start_vertex: int) -> Graph:
    """Search tree in graph"""
    queue_ = SimpleQueue()
    is_seen = {}

    frame = []

    queue_.put(start_vertex)
    is_seen[start_vertex] = True
    while not queue_.empty() :
        to_see = queue_.get()

        for neigbour in graph.get_neighbours(to_see):
            if neigbour not in is_seen:
                frame.append((to_see, neigbour))

                queue_.put(neigbour)
                is_seen[neigbour] = True

    return Graph(frame)


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

    # edges = [
    #     (1, [2, 4]),
    #     (2, [5, 3]),
    #     (3, [6, 4]),
    #     (4, [6, 7]),
    #     (5, [8, 9, 6]),
    #     (6, 7),
    # ]

    graph = Graph(edges, is_oriented=False)
    # or_graph = Graph(edges)

    print('Original graph')
    graph.show_graph()
    print()
    # or_graph.show_graph()
    # print()

    print('Frame graph')
    frame_graph = graph_frame_breadth_first_search(graph, 1)
    # frame_graph = graph_frame_breadth_first_search(or_graph, 1)
    frame_graph.show_graph()
