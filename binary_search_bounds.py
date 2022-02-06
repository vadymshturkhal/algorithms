def binary_search_bounds(sequence: list, element) -> tuple:
    left_bound = -1
    right_bound = len(sequence)

    return left_bound, right_bound


if __name__ == '__main__':
    a = [_ for _ in range(10)]
    print(binary_search_bounds(a, 11))
