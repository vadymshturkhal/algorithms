def show_permutations_min_transpositions(sequence: list, length: int):
    if sequence is None:
        if length is None:
            length = 3
        sequence = [i + 1 for i in range(length)]

    if length is None:
        length = len(sequence)

    how_position = [1 for _ in range(length)]
    is_element_moves_forward = [True for _ in range(length)]


if __name__ == '__main__':
    pass
