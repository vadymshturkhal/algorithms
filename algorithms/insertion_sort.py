def insertion_sort(sequence: list, left_bound=None, right_bound=None):
    if left_bound is None:
        left_bound = 0
        right_bound = len(sequence)

    for i in range(left_bound + 1, right_bound):
        for j in range(i, left_bound, -1):
            if sequence[j - 1] > sequence[j]:
                sequence[j], sequence[j - 1] = sequence[j - 1], sequence[j]
            else:
                break


if __name__ == '__main__':
    a = [i for i in range(10, 0, -1)]
    insertion_sort(a)
    print(a)
