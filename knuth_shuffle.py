from random import randint


def knuth_shuffle(sequence: list):
    for i in range(len(sequence)):
        random_index = randint(0, i)
        sequence[i], sequence[random_index] = sequence[random_index], sequence[i]


if __name__ == '__main__':
    a = [_ for _ in range(10)]
    knuth_shuffle(a)
    print(a)
