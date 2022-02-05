def merge_sort(sequence: list, tmp: list = None, left_bound=None, right_bound=None):
    if tmp is None:
        tmp = [sequence[i] for i in range(len(sequence))]
        left_bound = 0
        right_bound = len(sequence)

    if left_bound + 1 == right_bound:
        return

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
    a = [i for i in range(10, 0, -1)]
    merge_sort(a)
    print(a)
