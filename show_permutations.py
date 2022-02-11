def show_permutations(length=3, symbols_quantity=3) -> None:
    pass


def reverse(sequence: list, length_to_reverse: int = None) -> None:
    if length_to_reverse is None:
        length_to_reverse = len(sequence)

    for i in range(length_to_reverse // 2):
        sequence[i], sequence[length_to_reverse - i - 1] = sequence[length_to_reverse - i - 1], sequence[i]


if __name__ == '__main__':
    a = [_ for _ in range(9)]
    reverse(a)
    print(a)
    show_permutations()

