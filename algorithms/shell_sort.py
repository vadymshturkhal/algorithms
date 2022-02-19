from random import shuffle


def shell_sort(sequence: list) -> None:
    pass


if __name__ == '__main__':
    SEQUENCE_LENGTH = 10
    a = [_ for _ in range(SEQUENCE_LENGTH)]
    shuffle(a)
    print(a)
    shell_sort(a)
    print(a)
