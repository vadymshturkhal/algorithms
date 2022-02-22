class UnionFind:
    # O(N)
    def __init__(self, length):
        # Set id of each object to itself
        self.__elements_id = [_ for _ in range(length)]

    # O(N)
    # Change all entries with p_id to q_id
    def union(self, p, q):
        p_id = self.__elements_id[p]
        q_id = self.__elements_id[q]

        for i in range(len(self.__elements_id)):
            if self.__elements_id[i] == p_id:
                self.__elements_id[i] = q_id

    def is_connected(self, p, q) -> bool:
        return self.__elements_id[p] == self.__elements_id[q]


if __name__ == '__main__':
    UNION_LENGTH = 10
    uf = UnionFind(UNION_LENGTH)
    to_union = [
        [0, 5],
        [5, 6],
        [6, 1],
        [1, 2],
        [2, 7],

        [8, 3],
        [3, 4],
        [4, 9]
    ]

    for p, q in to_union:
        uf.union(p, q)

    print(uf.is_connected(0, 9))
    print(uf.is_connected(8, 9))
