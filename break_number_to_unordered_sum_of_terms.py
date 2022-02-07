def break_number_to_unordered_sum_of_terms(number: int, terms=None):
    """
        Assume number >= 0.
        Default terms from 1 to number.
        Returns quantity of unordered sum of terms from "terms".
        Theorem:
            F(n: [n1, n2,...,nk]) = F(n - n1: [n1, n2,...,nk]) + F(n: [n2,...,nk])/
            F(0: [n1, n2,...,nk]) = 1.
            F(-n: [n1, n2,...,nk]) = 0.
        Theorem:
            F(n: [n1, n2,...,nk]) = ?. Theorem doesn't exist.
        Theorem Hardy–Ramanujan:
            F(n: [n1, n2,...,nk]) ~ 1 / (4*n*sqrt(3)) * e**(pi*sqrt(2/3)*sqrt(n - 1/24)
    """

    if number == 0:
        return 1
    if number < 0:
        return 0

    if terms is None:
        terms = [_ for _ in range(1, number + 1)]

    if len(terms) <= 0:
        return 0

    f = break_number_to_unordered_sum_of_terms

    return f(number - terms[0], terms) + f(number, terms[1:])


if __name__ == '__main__':
    # For N = 3:
    # (1, 1, 1)
    # (1, 2)
    # (3)
    N = 3
    quantity = break_number_to_unordered_sum_of_terms(N)
    print(quantity)

    # For N = 6:
    # (1, 1, 1, 1, 1, 1)
    # (1, 1, 1, 1, 2)
    # (1, 1, 1, 3)
    # (1, 1, 4)
    # (1, 5)
    # (2, 2, 1, 1)
    # (2, 2, 2)
    # (2, 3, 1)
    # (3, 3)
    # (4, 2)
    # (6)
    N = 6
    quantity = break_number_to_unordered_sum_of_terms(N)
    print(quantity)
