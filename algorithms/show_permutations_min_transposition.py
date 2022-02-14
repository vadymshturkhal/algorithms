def show_permutations_min_transpositions(sequence: list = None, length: int = None):
    """Permutation can illustrates Hamiltonian path"""
    if sequence is None:
        if length is None:
            length = 3
        sequence = [i + 1 for i in range(length)]

    if length is None:
        length = len(sequence)

    how_position = [0 for _ in range(length)]
    is_element_moves_forward = [True for _ in range(length)]

    how_position[length - 1] = 0
    print(sequence)

    i = 0
    while i < length:
        i = 0
        x = 0
        while how_position[i] == length - i - 1:
            is_element_moves_forward[i] = not is_element_moves_forward[i]
            how_position[i] = 0

            if is_element_moves_forward[i]:
                x += 1

            i += 1
            if i >= length:
                break

        if i < length:
            if is_element_moves_forward[i]:
                k = how_position[i] + x
            else:
                k = length - i - 2 - how_position[i] + x

            sequence[k], sequence[k + 1] = sequence[k + 1], sequence[k]
            print(sequence)
            how_position[i] = how_position[i] + 1


if __name__ == '__main__':
    show_permutations_min_transpositions(length=4)
