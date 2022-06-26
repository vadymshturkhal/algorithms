from typing import Union
from math import comb


def comb_visual_improved(length: int, subset_length: int) -> Union[int, None]:
    """Visualize math.comb in lexicographic order"""
    current_subset = [i + 1 for i in range(subset_length)]

    counter = 0
    if subset_length > length:
        return counter

    if subset_length == length:
        counter += 1
        return counter

    pointer = subset_length - 1
    while 0 <= pointer:
        print(*current_subset)
        counter += 1

        if current_subset[subset_length - 1] == length:
            pointer -= 1
        else:
            pointer = subset_length - 1

        if 0 <= pointer:
            for i in range(subset_length - 1, pointer - 1, -1):
                current_subset[i] = current_subset[pointer] + i - pointer + 1

    return counter


if __name__ == '__main__':
    N = 5
    K = 3
    
    print(f"{comb_visual_improved(N, K) = }")
    print(f"{comb(N, K) = }")
