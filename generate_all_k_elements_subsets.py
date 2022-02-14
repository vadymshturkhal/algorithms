def generate_all_k_elements_subsets(length: int, subset_length: int) -> None:
    current_subset = [i + 1 for i in range(subset_length)]

    p = subset_length - 1
    while 0 <= p:
        print(current_subset)

        if current_subset[subset_length - 1] == length:
            p -= 1
        else:
            p = subset_length - 1

        if 0 <= p:
            for i in range(subset_length - 1, p - 1, -1):
                current_subset[i] = current_subset[p] + i - p + 1


if __name__ == '__main__':
    generate_all_k_elements_subsets(6, 4)
