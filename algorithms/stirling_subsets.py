def stirling_subsets(length: int):
    elements = [_ for _ in range(1, length + 1)]
    print(elements)

    cursor = length - 1

    # if cursor move forward 
    # then move forward (123)(4)

if __name__ == '__main__':
    SEQUENCE_LENGTH = 4

    """
        Must be:
            (1234)
            (123)(4)
            (12)(3)(4
            (12)(34)
            (124)(3)
            (14)(2)(3
            (1)(24)(3
            (1)(2)(34
            (1)(2)(3) 4)
            (1)(23)(4
            (1)(234)
            (14)(23)
            (134)(2)
            (13)(24)
            (13)(2)(4)
    """
    stirling_subsets(SEQUENCE_LENGTH)
