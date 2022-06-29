from comb_visual_generators import comb_visual_generators

def stirling_subsets(length: int):
    start = 1
    elements = [_ for _ in range(start, length + start)]

    for i in range(length // 2 + 1):
        how_many_elements_to_choose = length - i

        comb_gen = comb_visual_generators(elements, how_many_elements_to_choose)

        for current_combination in comb_gen:
            print('(', *current_combination, ')', sep='', end='')

            diff = set(elements).difference(current_combination)
            if len(diff) > 0:
                print('(', *diff, ')', sep='')
            else:
                print()



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
