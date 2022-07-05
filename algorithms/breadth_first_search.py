from operator import ne
from data_structures.graph import Graph
from queue import SimpleQueue, Queue


def breadth_first_search(graph: Graph, from_: int, to_: int) -> bool:
    queue_ = SimpleQueue()
    is_seen = {}

    queue_.put(from_)
    is_seen[from_] = True
    while not queue_.empty() :
        to_see = queue_.get()

        for neigbour in graph.get_neighbours(to_see):
            if neigbour not in is_seen:
                queue_.put(neigbour)
                is_seen[neigbour] = True

                if neigbour == to_:
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

    graph = Graph(edges, is_oriented=False)
    or_graph = Graph(edges)
    # graph.show_graph()
    # or_graph.show_graph()
    # print()

    print(f'{breadth_first_search(graph, 1, 11) = }')  # must be True
    print(f'{breadth_first_search(graph, 1, 16) = }')  # must be False

    print(f'{breadth_first_search(or_graph, 1, 9) = }')  # must be True
    print(f'{breadth_first_search(or_graph, 1, 16) = }')  # must be False
