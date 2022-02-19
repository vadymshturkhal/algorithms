from random import shuffle


def shell_sort(sequence: list) -> None:
    h = 1
    # Used 3x + 1 increment sequence.
    while h < len(sequence) / 3:
        h = 3 * h + 1

    while h >= 1:
        # Insertion sort,
        for i in range(len(sequence)):
            for j in range(i, h - 1, -h):
                if sequence[j] < sequence[j - h]:
                    sequence[j], sequence[j - h] = sequence[j - h], sequence[j]
        h //= 3


if __name__ == '__main__':
    SEQUENCE_LENGTH = 10
    a = [_ for _ in range(SEQUENCE_LENGTH)]
    shuffle(a)
    print(a)
    shell_sort(a)
    print(a)
