def generate_all_subsets(power: int):
    """Gray code"""
    subset = [0 for _ in range(power)]
    generated_subsets_quantity = 0

    p = 0
    j = 1
    print(subset)
    generated_subsets_quantity += 1

    while j % 2 == 0:
        j = j // 2
        p += 1

    if p <= power:
        subset[p] = 1 - subset[p]

    print(subset)


if __name__ == '__main__':
    POW = 4
    generate_all_subsets(POW)
