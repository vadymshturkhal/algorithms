def show_permutations_anti_lexicographic(sequence=None, length=3) -> None:
    if sequence is None:
        sequence = [i + 1 for i in range(length)]

    if length == 0:
        print(sequence)
        return
    else:
        for i in range(length):
            show_permutations_anti_lexicographic(sequence, length - 1)
            if i < length - 1:
                sequence[i], sequence[length - 1] = sequence[length - 1], sequence[i]
                reverse(sequence, length - 1)


def reverse(sequence: list, length_to_reverse: int = None) -> None:
    if length_to_reverse is None:
        length_to_reverse = len(sequence)

    for i in range(length_to_reverse // 2):
        sequence[i], sequence[length_to_reverse - i - 1] = sequence[length_to_reverse - i - 1], sequence[i]


if __name__ == '__main__':
    a = [_ for _ in range(9)]

    show_permutations()

