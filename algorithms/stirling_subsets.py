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
    merged = merge(subset, element_to_union)
    return merged

def merge(partitions: tuple, to_union: tuple) -> set:
    new_set = set()
    for partition in partitions:
        # print(partition)
        # new_set.add(union_all_sets(partition, to_union))

        # found bug frozenset({3}) frozenset({frozenset({2}), frozenset({1})})
        new_set.add(add_to_set(partition, to_union))  # works fine
    return new_set

def union_all_sets(sets: frozenset, to_union: set) -> frozenset:
    assert type(sets) == frozenset
    """
        Example:
            subset: {1, 2, 3}
            to_union: {4}
            result: ({1, 2, 3, 4}, )
    """
    # print(sets)
    # print(to_union, type(to_union))
    # print(sets.union(to_union))
    result_set = set()
    for subset in sets:
        if type(subset) != frozenset:
            return sets.union(to_union)

        # Each merge
        # {(1), (2 3)} {(1 3), (2)}
        print(subset)

def add_to_set(subset: tuple, to_add: tuple) -> tuple:
    """
        Example:
            subset: (1, 2, 3)
            to_add: (4,)
            result: ((1, 2, 3), (4,))
    """
    # if subset is tuple (1, 2, 3)
    if type(subset[0]) != tuple:
        added = [subset, to_add]
        added = tuple(added)
        return added
    
    # if subset is tuple of tuples ((1,), (2,), (3,))
    added = [* subset, to_add]
    added = tuple(added)
    return added

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
    # all_subsets = stirling_subsets(SEQUENCE_LENGTH)
    # print(all_subsets)

    result = merge([(1, 2), ((1,), (2,))], (3,))
    # print(result)

    for res in result:
        print(*res)
