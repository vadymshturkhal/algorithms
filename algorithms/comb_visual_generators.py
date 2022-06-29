from typing import Union
from math import comb


def comb_visual_generators(elements: int, subset_length: int) -> Union[int, None]:
    """Visualize math.comb in lexicographic order"""
    is_print_elements = False
    if type(elements) == list or type(elements) == set:
        length = len(elements)
        is_print_elements = True
    else:
        length = elements
    current_subset = [i + 1 for i in range(subset_length)]

    counter = 0
    if subset_length > length:
        return counter

    if subset_length == length:
        counter += 1
        yield current_subset
        return counter

    pointer = subset_length - 1
    while 0 <= pointer:
        if is_print_elements:
            current_state = [elements[current_subset[i] - 1] for i in range(len(current_subset))]
            yield current_state
        else:
            yield current_subset

        counter += 1

        if current_subset[subset_length - 1] == length:
            pointer -= 1
        else:
            pointer = subset_length - 1

        if 0 <= pointer:
            for i in range(subset_length - 1, pointer - 1, -1):
                current_subset[i] = current_subset[pointer] + i - pointer + 1

    return counter


if __name__ == '__main__':
    ELEMENTS = ['a', 'b', 'c', 'd', 'e', 1, 2, 3]
    K = 4

    comb_gen = comb_visual_generators(ELEMENTS, K)
    print(next(comb_gen))
    print(next(comb_gen))

    for i in comb_gen:
        print(i)
