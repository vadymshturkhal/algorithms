class UnionQuick:
    # O(1)
    def __init__(self):
        self.__elements_id = {}

    # O(Vertices)
    def union(self, edge):
        """Change all entries with start_parent to end_parent"""

        if len(edge) != 2:
            return

        self.__ensure_edge_vertices(edge)
        start, end = edge

        start_parent = self.__get_root(start)
        end_parent = self.__get_root(end)
        self.__elements_id[start_parent] = self.__elements_id[end_parent]

    # O(1)
    def is_connected(self, edge) -> bool:
        start, end = edge
        return self.__get_root(start) == self.__get_root(end)

    def show_union(self):
        for vertex, id in self.__elements_id.items():
            print(vertex, id)

    def __get_root(self, vertex):
        while vertex != self.__elements_id.get(vertex, vertex):
            self.__elements_id[vertex] = self.__elements_id[self.__elements_id[vertex]]
            vertex = self.__elements_id[vertex]

        return vertex

    def __ensure_edge_vertices(self, edge):
        """Set id of each object to itself"""

        start, end = edge
        if start not in self.__elements_id:
            self.__elements_id[start] = start

        if end not in self.__elements_id:
            self.__elements_id[end] = end


if __name__ == '__main__':
    to_union = [
        [4, 3],
        [3, 8],
        [6, 5],
        [9, 4],
        [2, 1],
        [5, 0],
        [7, 2],
        [6, 1],
        [7, 3],
    ]

    union_find_quick = UnionQuick()

    for edge in to_union:
        union_find_quick.union(edge)

    union_find_quick.show_union()
    print(union_find_quick.is_connected((7, 8)))
    print(union_find_quick.is_connected((17, 8)))
