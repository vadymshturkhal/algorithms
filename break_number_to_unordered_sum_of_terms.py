def break_number_to_unordered_sum_of_pairs(number: int, terms=None):
    """
        Assume number >= 0.
        Default terms from 1 to number.
        Returns quantity of unordered sum of terms from "terms".
        Theorem:
            F(n: [n1, n2,...,nk]) = F(n - n1: [n1, n2,...,nk]) + F(n: [n2,...,nk])
        Theorem:
            F(n: [n1, n2,...,nk]) = ?. Theorem doesn't exist.
        Theorem Hardy–Ramanujan:
            F(n: [n1, n2,...,nk]) ~ 1 / (4*n*sqrt(3)) * e**(pi*sqrt(2/3)*sqrt(n - 1/24)
    """

    if terms is None:
        terms = [_ for _ in range(1, number + 1)]

    return 0


if __name__ == '__main__':
    N = 3
    quantity = break_number_to_unordered_sum_of_pairs(N)
    print(quantity)
