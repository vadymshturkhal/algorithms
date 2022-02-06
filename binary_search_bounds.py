def binary_search_bounds(sequence: list, element) -> tuple:
    left_bound = search_bounds(sequence, element, left_bound_searching=True)
    right_bound = search_bounds(sequence, element, left_bound_searching=False)

    return left_bound, right_bound


def search_bounds(sequence: list, element, left_bound_searching=True):
    left_bound = -1
    right_bound = len(sequence)

    if left_bound_searching:
        while right_bound - left_bound != 1:
            mid = (right_bound + left_bound) // 2
            if sequence[mid] < element:
                left_bound = mid
            else:
                right_bound = mid

        return left_bound

    while right_bound - left_bound != 1:
        mid = (right_bound + left_bound) // 2
        if sequence[mid] <= element:
            left_bound = mid
        else:
            right_bound = mid

    return right_bound


if __name__ == '__main__':
    a = [1, 1, 1, 3, 4, 5]
    print(binary_search_bounds(a, 1))
