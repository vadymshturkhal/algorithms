from stirling_numbers_second_kind import stirling_nums_second

"""
    Show Bell's numbers of N.
    Which equals to sum of S(N, i) from i = 0 to i = N.
    S = Stirling numbers of second kind.
"""

def stirling_subsets(elements, to_union=None, default_start=1) -> list:
    if type(elements) == list:
        length = len(elements)
    else:
        length = elements
        elements = [_ for _ in range(default_start, length + default_start)]

    if len(elements) <= 1:
        elements = tuple(elements)
        return [elements]

    # must be a set
    element_to_union = (elements.pop(),)
    subset = stirling_subsets(elements, element_to_union)
    merged = merge(subset, element_to_union)

    # print(subset, element_to_union)
    # print(merged)

    return merged

def merge(partitions: tuple, to_union: tuple) -> list:
    new_partitions = []
    for partition in partitions:
        # print('p',partition)

        gen = union_all_sets(partition, to_union)
        for subset in gen:
            # print(subset)
            new_partitions.append(subset)

        # print('after union')

        x = add_to_set(partition, to_union)

        # print(x)
        # print('after add_to_set')

        new_partitions.append(x)  # works fine

    # print(new_set)
    # print()

    return new_partitions

def merge_tuples(first: tuple, second: tuple) -> tuple:
    first = set(first)
    second = set(second)
    merged = first.union(second)
    tuple_merged = tuple(merged)
    return tuple_merged

def union_all_sets(subset: tuple, to_union: tuple) -> tuple:
    """
        Example:
            subset: (1, 2, 3)
            to_union: (4,)
            result: (1, 2, 3, 4)
    """
    # print(subset, to_union)
    # if subset is tuple (1, 2, 3)
    if not is_tuple_of_tuples(subset):
        added = (sorted([*subset, *to_union]))
        added = tuple(added)
        # print(added, subset, to_union)
        yield added
        return

    # if subset is tuple of tuples ((1,), (2,), (3,))
    subsets = set(subset)
    for subset in subsets:
        subset_to_compare = set((subset, ))
        difference = subsets.difference(subset_to_compare)
        merged = merge_tuples(subset, to_union)

        added = add_to_set(sorted([merged, *difference]))
        yield added
    return

def add_to_set(subset: tuple, *to_add: tuple) -> tuple:
    """
        Example:
            subset: (1, 2, 3)
            to_add: (4,)
            result: ((1, 2, 3), (4,))
    """
    # if subset is tuple (1, 2, 3)
    if not is_tuple_of_tuples(subset):
        added = [subset, *to_add]
        added = tuple(added)
        return added
    
    # if subset is tuple of tuples ((1,), (2,), (3,))
    added = [*subset, *to_add]
    added = tuple(added)
    return added

def is_tuple_of_tuples(subset):
    return type(subset[0]) == tuple

def bell_number(n):
    bell_num = 0
    for i in range(n + 1):
        bell_num += stirling_nums_second(n, i)
    return bell_num


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

    all_subsets = stirling_subsets(SEQUENCE_LENGTH)
    # print(all_subsets)
    for subset in all_subsets:
        print(subset)

    bell_num = bell_number(SEQUENCE_LENGTH)  # should be 15
    print(f'Bell num for {SEQUENCE_LENGTH} = {bell_num}')

    bell_num = bell_number(5)  # should be 52
    print(f'Bell num for {5} = {bell_num}')

    bell_num = bell_number(10)  # should be 115975
    print(f'Bell num for {10} = {bell_num}')
