import random
from insertion_sort import insertion_sort

CUTOFF = 5


def quick_sort_insertion(sequence: list, low: int = None, high: int = None):
    if low is None and high is None:
        low = 0
        high = len(sequence) - 1

        # Shuffle needed for performance guarantee
        random.shuffle(sequence)

    if high <= low + CUTOFF:
        insertion_sort(sequence, low, high)
        return

    correct_position_index = partition(sequence, low, high)
    quick_sort_insertion(sequence, low, correct_position_index - 1)
    quick_sort_insertion(sequence, correct_position_index + 1, high)


def partition(sequence: list, low: int, high: int):
    i = low + 1
    j = high

    while True:
        while sequence[i] < sequence[low]:
            i += 1
            if i >= high:
                break

        while sequence[low] < sequence[j]:
            j -= 1
            if j <= low:
                break

        if i >= j:
            break
        sequence[i], sequence[j] = sequence[j], sequence[i]

    sequence[low], sequence[j] = sequence[j], sequence[low]
    return j


if __name__ == '__main__':
    a = [_ for _ in range(20, -1, -1)]
    quick_sort_insertion(a)
    print(a)
