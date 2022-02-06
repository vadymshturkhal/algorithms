# Use insertion sort for small arrays.
# ・ Mergesort has too much overhead for tiny arrays.
# ・ Cutoff to insertion sort for ≈ 7 item

CUTOFF = 7


def insertion_sort(sequence: list, left_bound=None, right_bound=None):
    if left_bound is None:
        left_bound = 0
        right_bound = len(sequence)

    for i in range(left_bound, right_bound):
        for j in range(i, 0, -1):
            if sequence[j - 1] > sequence[j]:
                sequence[j], sequence[j - 1] = sequence[j - 1], sequence[j]
            else:
                break


def merge_sort(sequence: list, tmp: list = None, left_bound=None, right_bound=None):
    if tmp is None:
        tmp = [sequence[i] for i in range(len(sequence))]
        left_bound = 0
        right_bound = len(sequence)

    if left_bound + CUTOFF - 1 >= right_bound:
        print(right_bound - left_bound)
        insertion_sort(sequence, left_bound, right_bound)
        return

    if left_bound + CUTOFF <= right_bound:
        insertion_sort(sequence)

    mid = (left_bound + right_bound) // 2

    merge_sort(tmp, sequence, left_bound, mid)
    merge_sort(tmp, sequence, mid, right_bound)

    sequence, tmp = tmp, sequence
    merge(sequence, tmp, left_bound, mid, right_bound)


def merge(sequence: list, tmp: list, left_bound, mid, right_bound):
    left_counter = left_bound
    right_counter = mid

    for i in range(left_bound, right_bound):
        if mid <= left_counter:
            tmp[i] = sequence[right_counter]
            right_counter += 1
        elif right_bound <= right_counter:
            tmp[i] = sequence[left_counter]
            left_counter += 1
        elif sequence[left_counter] <= sequence[right_counter]:
            tmp[i] = sequence[left_counter]
            left_counter += 1
        else:
            tmp[i] = sequence[right_counter]
            right_counter += 1


if __name__ == '__main__':
    a = [i for i in range(100, 0, -1)]
    merge_sort(a)
    print(a)
