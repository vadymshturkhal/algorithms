from count_inversions import count_inversions_quadratic


def sign_of_sequence(sequence: list) -> int:
    """Sign of sequence equals to (-1)**(sequence inversions)"""
    return (-1) ** count_inversions_quadratic(sequence)


def is_even_permutation(sequence: list) -> bool:
    pass


if __name__ == '__main__':
    a = [7, 5, 1, 4, 2, 3, 6]
    sign = sign_of_sequence(a)
    print(sign)
