def count_inversions(sequence: list) -> int:
    """Max inversions quantity equals to n*(n - 1)/2."""

    inversions_quantity = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] > sequence[j]:
                inversions_quantity += 1
    return inversions_quantity


if __name__ == '__main__':
    N = 10
    # a = [_ for _ in range(N, 0, -1)]
    inversions = count_inversions(a)
    print(inversions)
