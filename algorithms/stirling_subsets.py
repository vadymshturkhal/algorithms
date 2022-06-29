from comb_visual_generators import comb_visual_generators

def stirling_subsets(elements, to_print=None, default_start=1):
    if type(elements) == list:
        length = len(elements)
    else:
        length = elements
        elements = [_ for _ in range(default_start, length + default_start)]

    if len(elements) == 2:
        if to_print:
            print(tuple(to_print), tuple(elements))
            print(tuple(to_print), f'({elements[0]}) ({elements[1]})')
        else:
            print(tuple(elements))
            print(f'({elements[0]}) ({elements[1]})')
        return
    
    if len(elements) <= 1:
        return

    for i in range(length // 2 + 1):
        i = length - i
        comb_gen = comb_visual_generators(elements, i)

        for current_combination in comb_gen:
            diff = set(elements).difference(current_combination)

            # default
            # print(current_combination, diff)
            if len(diff) == 0:
                print(current_combination)
            elif len(diff) == 1:
                print(current_combination, f'({diff.pop()})');
            else:  # len(diff) >= 2
                stirling_subsets(list(diff), to_print=current_combination)

            # for avoid 
            # (1)(2)
            # (2)(1)
            if len(elements) <= 2:
                break


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
