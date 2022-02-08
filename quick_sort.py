def quick_sort(sequence: list):
    pass


def partition(sequence: list, low: int, high: int):
    i = low
    j = high

    while True:
        while sequence[i] < sequence[low]:
            i += 1
            if i == high:
                break

        while sequence[low] < sequence[j]:
            j -= 1
            if j == low:
                break

        if i >= j:
            break
        sequence[i], sequence[j] = sequence[j], sequence[i]

    sequence[low], sequence[j] = sequence[j], sequence[low]


if __name__ == '__main__':
    a = [_ for _ in range(10, -1, -1)]
    partition(a, 0, len(a) - 1)
    print(a)
