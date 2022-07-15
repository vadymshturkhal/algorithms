class UnionQuick:
    # O(1)
    def __init__(self):
        self.__elements_id = {}
        self.__sizes = {}

    def union(self, edge):
        """The smaller tree goes below"""
        if len(edge) != 2:
            return

        self.__ensure_edge_vertices(edge)
        start, end = edge

        start_parent = self.__get_root(start)
        end_parent = self.__get_root(end)

        if start_parent == end_parent:
            return

        self.__ensure_sizes(start_parent, end_parent)

        start_income = self.__sizes[self.__elements_id[start_parent]]
        end_income = self.__sizes[self.__elements_id[end_parent]]

        if start_income < end_income:
            self.__sizes
            # self.__sizes[self.__elements_id[end_parent]] += 1
            # self.__sizes[self.__elements_id[start_parent]] -= 1
            self.__sizes[self.__elements_id[end_parent]] += self.__sizes[self.__elements_id[start_parent]]
            self.__elements_id[start_parent] = self.__elements_id[end_parent]
        else:
            # self.__sizes[self.__elements_id[end_parent]] -= 1
            # self.__sizes[self.__elements_id[start_parent]] += 1
            self.__sizes[self.__elements_id[start_parent]] += self.__sizes[self.__elements_id[end_parent]]
            self.__elements_id[end_parent] = self.__elements_id[start_parent]

    # O(1)
    def is_connected(self, edge) -> bool:
        start, end = edge
        return self.__get_root(start) == self.__get_root(end)

    def show_union(self):
        for vertex, id in self.__elements_id.items():
            print(vertex, id)

    def show_sizes(self):
        print(self.__sizes)

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

    def __ensure_sizes(self, *vertices):
        for vertex in vertices:
            if self.__elements_id[vertex] not in self.__sizes:
                self.__sizes[vertex] = 1


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
    union_find_quick.show_sizes()

    print(union_find_quick.is_connected((7, 8)))
    print(union_find_quick.is_connected((17, 8)))