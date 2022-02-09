import time
from merge_sort import merge_sort
from merge_sort_insertion import merge_sort_insertion
from quick_sort import quick_sort
from quick_sort_insertion import quick_sort_insertion
from insertion_sort import insertion_sort

ARRAY_LENGTH = 5000

SORTS = {
    'Timsort             ': list.sort,
    'merge_sort          ': merge_sort,
    'merge_sort_insertion': merge_sort_insertion,
    'quick_sort          ': quick_sort,
    'quick_sort_insertion': quick_sort_insertion,
    'insertion_sort      ': insertion_sort,
}

for name, sort in SORTS.items():
    array_to_sort = [_ for _ in range(ARRAY_LENGTH, 0, -1)]
    start_time = time.time()
    sort(array_to_sort)
    print(name, time.time() - start_time)
