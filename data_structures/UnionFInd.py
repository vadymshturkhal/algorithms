class UnionFind:
    def __init__(self, length):
        pass

    def union(self, p, q):
        pass

    def is_connected(self, p, q):
        pass


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
