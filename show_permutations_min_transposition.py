def show_permutations_min_transpositions(sequence: list = None, length: int = None):
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
    counter = 1

    i = 0
    length -= 1
    while i < length:
        i = 0
        x = 0
        while how_position[i] == length - i:
            is_element_moves_forward[i] = not is_element_moves_forward[i]
            how_position[i] = 0

            if is_element_moves_forward[i]:
                x += 1

            i += 1

        if i < length:
            if is_element_moves_forward[i]:
                k = how_position[i] + x
            else:
                k = length - 1 - i - how_position[i] + x

            sequence[k], sequence[k + 1] = sequence[k + 1], sequence[k]
            print(sequence)
            counter += 1
            how_position[i] = how_position[i] + 1
            print(counter)


if __name__ == '__main__':
    show_permutations_min_transpositions(length=4)
