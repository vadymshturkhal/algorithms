def generate_all_k_elements_subsets(length: int, subset_length: int) -> None:
    if subset_length > length:
        return

    current_subset = [i + 1 for i in range(subset_length)]

    if subset_length == length:
        print(current_subset)
        return

    pointer = subset_length - 1
    while 0 <= pointer:
        print(*current_subset)

        if current_subset[subset_length - 1] == length:
            pointer -= 1
        else:
            pointer = subset_length - 1

        if 0 <= pointer:
            for i in range(subset_length - 1, pointer - 1, -1):
                current_subset[i] = current_subset[pointer] + i - pointer + 1


if __name__ == '__main__':
    generate_all_k_elements_subsets(4, 3)
