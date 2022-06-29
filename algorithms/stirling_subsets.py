def stirling_subsets(length: int):
    start = 1
    elements = [_ for _ in range(start, length + start)]
    is_move_forward = [True for _ in range(length)]
    print(elements)

    cursor = length - 1

    # if cursor move forward 
    # then move forward (123)(4)
    if is_move_forward[cursor]:
        element = elements[cursor]
    
    print(elements[:cursor], [element])
    # print(cursor, cursor + start)
    while cursor > 0 and is_move_forward[cursor] and elements[cursor] == (cursor + start):
        # print(cursor, is_move_forward[cursor])
        is_move_forward[cursor] = not is_move_forward
        # print(cursor, is_move_forward[cursor])

        cursor -= 1

    # print(cursor)


if __name__ == '__main__':
    SEQUENCE_LENGTH = 4

    """
        Must be:
            (1234)
            (123)(4)
            (12)(3)(4)
            (12)(34)
            (124)(3)
            (14)(2)(3)
            (1)(24)(3)
            (1)(2)(34)
            (1)(2)(3)(4)
            (1)(23)(4)
            (1)(234)
            (14)(23)
            (134)(2)
            (13)(24)
            (13)(2)(4)
    """
    stirling_subsets(SEQUENCE_LENGTH)
