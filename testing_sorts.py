import time
from merge_sort import merge_sort
from merge_sort_insertion import merge_sort_insertion
from quick_sort import quick_sort

N = 900

a = [_ for _ in range(N, -1, -1)]
x = time.time()
merge_sort(a)
print("merge_sort", time.time() - x)
print()

a = [_ for _ in range(N, -1, -1)]
x = time.time()
merge_sort_insertion(a)
print("merge_sort_insertion", time.time() - x)
print()

a = [_ for _ in range(N, -1, -1)]
x = time.time()
quick_sort(a)
print("quick_sort", time.time() - x)
