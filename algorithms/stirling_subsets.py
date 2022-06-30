from comb_visual_generators import comb_visual_generators

def stirling_subsets(elements, to_union=None, default_start=1):
    if type(elements) == list:
        length = len(elements)
    else:
        length = elements
        elements = [_ for _ in range(default_start, length + default_start)]

    if len(elements) <= 1:
        elements = {frozenset(elements)}
        return elements

    # must be a set
    element_to_union = frozenset([elements.pop()])
    subset = stirling_subsets(elements, element_to_union)
    unioned = invariant(subset, element_to_union)
    return unioned

def invariant(partitions: list, to_union):
    new_set = set()
    for partition in partitions:
        # print(partition)
        new_set.add(union_sets(partition, to_union))
        new_set.add(add_to_set(partition, to_union))
    return new_set

def union_sets(subset: set, to_union: set) -> frozenset:
    """
        Example:
            subset: {1, 2, 3}
            to_union: {4}
            result: ({1, 2, 3, 4}, )
    """
    return subset.union(to_union)

def add_to_set(subset: frozenset, to_add: frozenset) -> frozenset:
    """
        Example:
            subset: {1, 2, 3}
            to_add: {4}
            result: ({1, 2, 3}, {4})
    """
    return frozenset([subset, to_add])

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
    all_subsets = stirling_subsets(SEQUENCE_LENGTH)
    print(all_subsets)
