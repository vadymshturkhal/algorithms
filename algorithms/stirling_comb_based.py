from comb_visual_generators import comb_visual_generators

def stirling_subsets(elements, to_union=None, default_start=1):
    if type(elements) == list:
        length = len(elements)
    else:
        length = elements
        elements = [_ for _ in range(default_start, length + default_start)]

    four = comb_visual_generators(elements, 4)
    for i in four:
        print(i)

    three = comb_visual_generators(elements, 3)
    for i in three:
        print(i, set(elements).difference(i))

    two = comb_visual_generators(elements, 2)
    for i in two:
        print(i, set(elements).difference(i))


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
    # stirling_subsets(SEQUENCE_LENGTH)
    stirling_subsets(SEQUENCE_LENGTH)