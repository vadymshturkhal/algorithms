def binary_search(sequence: list) -> tuple:
    left_bound = 0
    right_bound = len(sequence) - 1

    return left_bound, right_bound


if __name__ == '__main__':
    a = [_ for _ in range(10)]
    bounds = binary_search(a)
    print(bounds)
