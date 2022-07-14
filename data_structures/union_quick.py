class UnionQuick:
    # O(1)
    def __init__(self):
        self.__elements_id = {}

    # O(Vertices)
    def union(self, edge):
        """Change all entries with start_id to end_id"""

        if len(edge) != 2:
            return

        self.__ensure_edge_vertices(edge)
        start, end = edge

        start_id = self.__elements_id[start]
        end_id = self.__elements_id[end]

        while start_id != self.__elements_id[start_id]:
            start_id = self.__elements_id[start_id]

        self.__elements_id[start_id] = self.__elements_id[end_id]

    # O(1)
    def is_connected(self, edge) -> bool:
        start, end = edge
        return self.__elements_id.get(start, start) == self.__elements_id.get(end, end)

    def show_union(self):
        for vertex, id in self.__elements_id.items():
            print(vertex, id)

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

    print(union_find_quick.is_connected((3, 8)))  # must be True
    print(union_find_quick.is_connected((1, 8)))  # must be False
    union_find_quick.show_union()
