from random import shuffle


def selection_sort(sequence: list) -> None:
    for i in range(len(sequence)):
        for j in range(len(sequence)):
            if sequence[i] < sequence[j]:
                sequence[i], sequence[j] = sequence[j], sequence[i]


if __name__ == '__main__':
    SEQUENCE_LENGTH = 10
    a = [_ for _ in range(SEQUENCE_LENGTH)]
    shuffle(a)
    print(a)
    selection_sort(a)
    print(a)
