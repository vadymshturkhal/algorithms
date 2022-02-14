from random import shuffle


def bubble_sort(sequence: list) -> None:
    for i in range(len(sequence)):
        for j in range(1, len(sequence)):
            if sequence[j - 1] > sequence[j]:
                sequence[j - 1], sequence[j] = sequence[j], sequence[j - 1]


if __name__ == '__main__':
    SEQUENCE_LENGTH = 10
    a = [_ for _ in range(SEQUENCE_LENGTH)]
    shuffle(a)
    print(a)
    bubble_sort(a)
    print(a)
