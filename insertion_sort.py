def insertion_sort(sequence: list):
    for i in range(1, len(sequence)):
        for j in range(i, 0, -1):
            if sequence[j - 1] > sequence[j]:
                sequence[j], sequence[j - 1] = sequence[j - 1], sequence[j]
            else:
                break


if __name__ == '__main__':
    a = [i for i in range(10, 0, -1)]
    insertion_sort(a)
    print(a)
