from count_inversions import count_inversions_quadratic


def sign_of_sequence_quadratic(sequence: list) -> int:
    """Sign of sequence equals to (-1)**(sequence inversions)"""
    return (-1) ** count_inversions_quadratic(sequence)


def sign_of_sequence_fast(sequence: list) -> int:
    """
        Sign of sequence equals to (-1)**(sequence inversions).
        Sequence must contain elements from 0 to len(sequence).
    """
    sign = 1
    elements_to_check = [True for _ in range(len(sequence))]

    for i in range(len(sequence)):
        if elements_to_check[i]:
            current_element = sequence[i]
            while current_element != i:
                elements_to_check[current_element] = False
                sign = -sign
                current_element = sequence[current_element]

    return sign


def is_even_permutation(sequence: list) -> bool:
    return True if sign_of_sequence_quadratic(sequence) == 1 else False


if __name__ == '__main__':
    a = [7, 5, 1, 4, 2, 3, 6, 0]
    print(sign_of_sequence_quadratic(a))
    print(is_even_permutation(a))

    a = [7, 5, 1, 4, 2, 3, 6, 0]
    print(sign_of_sequence_fast(a))
