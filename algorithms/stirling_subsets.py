from comb_visual_generators import comb_visual_generators

def stirling_subsets(elements, to_union=None, default_start=1):
    if type(elements) == list:
        length = len(elements)
    else:
        length = elements
        elements = [_ for _ in range(default_start, length + default_start)]

    if len(elements) <= 1:
        # return tuple of tuples for invariant
        return ((set(elements),),)

    to_union = elements.pop()
    x = stirling_subsets(elements, to_union)
    to_return = invariant(x, {to_union})
    return to_return

def invariant(partitions: list, to_union, unions=None):
    if unions is None:
        unions = []

    for part in partitions:
        if type(part) == list:
            invariant(part, to_union, unions)
        else:  # type(part) == tuple
            # print('part', part, 'to_union', to_union)
            add = add_to_set(part, to_union)
            union = union_sets(part, to_union)
            result = [union, add]
            unions.append(result)
    # print(unions)
    return unions

def union_sets(partition, to_union):
    """
        Example:
            partition: {1, 2, 3}
            to_union: {4}
            result: ({1, 2, 3, 4},)
    """
    u = []
    print(partition)
    for part in partition:
        to_add = part.union(to_union)
        u.append(part.union(to_union))
        print(part, to_union, u)

    return (*u,)

def add_to_set(partition, to_add):
    """
        Example:
            partition: {1, 2, 3}
            to_add: {4}
            result: ({1, 2, 3}, {4})
    """
    if len(partition) == 1:
        if type(partition) == set:
            partition = [partition]
    return (*partition, to_add)

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
