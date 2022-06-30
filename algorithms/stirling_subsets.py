from comb_visual_generators import comb_visual_generators

def stirling_subsets(elements, to_union=None, default_start=1):
    if type(elements) == list:
        length = len(elements)
    else:
        length = elements
        elements = [_ for _ in range(default_start, length + default_start)]

    if len(elements) <= 1:
        # x = tuple(elements)
        # if to_union is not None:
        #     to_return = invariant(x, {to_union})
        #     return to_return
        return (set(elements),)

    to_union = elements[-1]
    x = stirling_subsets(elements[:len(elements) - 1], to_union)
    to_return = invariant(x, {to_union})
    return to_return
    # return x
    # if len(elements) == 2:
    #     # if to_print:
    #     #     print(tuple(to_print), tuple(elements))
    #     #     print(tuple(to_print), f'({elements[0]}) ({elements[1]})')
    #     # else:
    #     #     print(tuple(elements))
    #     #     print(f'({elements[0]}) ({elements[1]})')
    #     all_partitions = (set(elements), (set([elements[0]]), set([elements[1]])))
    #     for partition in all_partitions:
    #         print(partition, type(partition) == tuple)
    #     return all_partitions


def invariant(partitions: list, to_union, unions=None):
    if unions is None:
        unions = []

    for part in partitions:
        if type(part) == set:

            x = union_sets(part, to_union)
            x1 = add_to_set(part, to_union)
            # print(x, x1)
            unions.append((x, x1))
            # return (x, x1)
        else:
            x = invariant(part, to_union, unions)
            print(part, to_union)

            # return x
    # print(unions)
    return unions

def union_sets(partition, to_union):
    """
        Example:
            partition: {1, 2, 3}
            to_union: {4}
            result: ({1, 2, 3, 4},)
    """
    # print((partition.union(to_union), ))
    return (partition.union(to_union), )

def add_to_set(partition, to_add):
    """
        Example:
            partition: {1, 2, 3}
            to_add: {4}
            result: ({1, 2, 3}, {4})
    """
    # print((partition, to_add))
    return (partition, to_add)

if __name__ == '__main__':
    SEQUENCE_LENGTH = 3

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
    x = stirling_subsets(SEQUENCE_LENGTH)
    print(x)
    # for i in x:
        # print(*i)
