def binary_search(sequence: list, element) -> int:
    left_bound = 0
    right_bound = len(sequence) - 1

    while left_bound <= right_bound:
        mid = (left_bound + right_bound) // 2
        if element < sequence[mid]:
            right_bound = mid - 1
        elif element > sequence[mid]:
            left_bound = mid + 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    a = [i + 1 for i in range(10)]
    print(binary_search(a, 9))
    print(binary_search(a, 10))
    print(binary_search(a, 11))
