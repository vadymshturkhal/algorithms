from algorithms.knuth_shuffle import knuth_shuffle
from data_structures.binary_heap import BinaryHeap


def heap_sort(sequence: list) -> None:
    bh = BinaryHeap(return_max=False)
    for item in sequence:
        bh.insert(item)

    for i in range(len(sequence)):
        sequence[i] = bh.del_element()


if __name__ == '__main__':
    SEQUENCE_LENGTH = 10
    a = [_ for _ in range(SEQUENCE_LENGTH, 0, -1)]
    knuth_shuffle(a)
    print(a)
    heap_sort(a)
    print(a)
