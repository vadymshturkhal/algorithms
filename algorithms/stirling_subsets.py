from comb_visual_generators import comb_visual_generators

def stirling_subsets(elements, to_print=None, default_start=1):
    if type(elements) == list:
        length = len(elements)
    else:
        length = elements
        elements = [_ for _ in range(default_start, length + default_start)]

    if len(elements) == 2:
        # if to_print:
        #     print(tuple(to_print), tuple(elements))
        #     print(tuple(to_print), f'({elements[0]}) ({elements[1]})')
        # else:
        #     print(tuple(elements))
        #     print(f'({elements[0]}) ({elements[1]})')
        all_partitions = (set(elements), (set([elements[0]]), set([elements[1]])))
        for partition in all_partitions:
            print(partition)
        return all_partitions


if __name__ == '__main__':
    SEQUENCE_LENGTH = 2

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
    # stirling_subsets(SEQUENCE_LENGTH)
    stirling_subsets(SEQUENCE_LENGTH)
