from random import shuffle


def selection_sort(sequence: list) -> None:
    pass


if __name__ == '__main__':
    SEQUENCE_LENGTH = 10
    a = [_ for _ in range(SEQUENCE_LENGTH)]
    shuffle(a)
    print(a)
    selection_sort(a)
    print(a)
