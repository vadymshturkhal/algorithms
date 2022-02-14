from count_inversions import count_inversions_quadratic
import time


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
    return True if sign_of_sequence_fast(sequence) == 1 else False


if __name__ == '__main__':
    SEQUENCE_LENGTH = 1111
    a = [_ for _ in range(SEQUENCE_LENGTH - 1, -1, -1)]

    time_begin = time.time()
    s = sign_of_sequence_quadratic(a)
    time_end = time.time() - time_begin
    print('sign_of_sequence_quadratic time: ', round(time_end, 8), 'sign = ', s)

    time_begin = time.time()
    s = sign_of_sequence_fast(a)
    time_end = time.time() - time_begin
    print('sign_of_sequence_fast time     : ', round(time_end, 8), 'sign = ', s)

    print(f'{is_even_permutation(a)=}')
