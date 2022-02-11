def show_permutations_anti_lexicographic_fast(sequence=None, length=None):
    if sequence is None:
        if length is None:
            length = 3
        sequence = [i + 1 for i in range(length)]

    if length is None:
        length = len(sequence)

    if length == 0:
        print(sequence)
        return
    else:
        for i in range(length):
            show_permutations_anti_lexicographic_fast(sequence, length - 1)
            if i < length - 1:
                sequence[length - 1], sequence[permutation_from_previous(length - 1, i)] = sequence[permutation_from_previous(
                    length - 1, i)], sequence[length - 1]


def permutation_from_previous(length, index):
    if length % 2 != 0 and length > 1:
        if index < length - 1:
            return index
        else:
            return length - 2
    else:
        return length - 1


if __name__ == '__main__':
    show_permutations_anti_lexicographic_fast(length=4)
