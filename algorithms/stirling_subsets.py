def stirling_subsets(length: int):
    partition = []
    forward = []
    next_partition = [0] * length

    for i in range(length):
        partition[i] = 1
        forward[i] = True

    pointer = length


if __name__ == '__main__':
    SEQUENCE_LENGTH = 4
    stirling_subsets(SEQUENCE_LENGTH)