from data_structures.binary_heap import BinaryHeap
from data_structures.priority_queue_unordered import UnorderedMaxPriorityQueue
from time import time

ITEMS_QUANTITY = 4000

bh = BinaryHeap()
unordered_max_pq = UnorderedMaxPriorityQueue()

data_structs = {
    "binary heap": bh,
    "unordered priority queue": unordered_max_pq
}

print(f"{ITEMS_QUANTITY = }")
for name, ds in data_structs.items():
    start_time = time()
    for i in range(ITEMS_QUANTITY):
        ds.insert(i)

    for i in range(ITEMS_QUANTITY):
        ds.del_element()

    elapsed_time = time() - start_time
    print(f"{name}, {elapsed_time = }")

