from operator import ne
from data_structures.graph import Graph
from queue import SimpleQueue, Queue


def breadth_first_search(graph: Graph, from_: int, to_: int, *, is_print_shortest_path: bool=False) -> bool:
    queue_ = SimpleQueue()
    is_seen = {}
    shortest_path = {}

    queue_.put(from_)
    is_seen[from_] = True
    while not queue_.empty() :
        to_see = queue_.get()

        for neigbour in graph.get_neighbours(to_see):
            if neigbour not in is_seen:
                queue_.put(neigbour)
                is_seen[neigbour] = True
                shortest_path[neigbour] = to_see

                if neigbour == to_:
                    if is_print_shortest_path:
                        print_shortest_path(shortest_path, neigbour)
                    return True
    return False

def print_shortest_path(messy_path, last_key_in_path):
    previous_key = messy_path[last_key_in_path]

    shortest_path = [last_key_in_path, previous_key]

    while previous_key in messy_path:
        previous_key = messy_path[previous_key]
        shortest_path.append(previous_key)
    
    shortest_path.reverse()
    print(shortest_path)


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
    # print()
    # or_graph.show_graph()
    # print()

    print(f'{breadth_first_search(graph, 1, 11, is_print_shortest_path=True) = }')  # must be True
    print(f'{breadth_first_search(graph, 1, 16) = }')  # must be False
    print()

    print(f'{breadth_first_search(or_graph, 1, 9, is_print_shortest_path=True) = }')  # must be True
    print(f'{breadth_first_search(or_graph, 1, 16, is_print_shortest_path=True) = }')  # must be False
