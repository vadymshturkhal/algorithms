def number_to_limited_sum_of_terms(number: int, terms: list):
    """
    Theorem:
        F(N: [n1, n2,...,nk]) = F(N - nk: [n1, n2,...,nk - 1]) + F(N: [n1, n2,...,nk - 1])
        F(0: [n1, n2,...,nk]) = 1.
        if N > sum([[n1, n2,...,nk]]): F(N: [n1, n2,...,nk]) = 0
        F(-n: [n1, n2,...,nk]) = 0.
    """
    terms = list(filter(lambda x: x <= number, terms))

    if number == 0:
        return 1

    if number > sum(terms):
        return 0

    if len(terms) <= 0:
        return 0

    F = number_to_limited_sum_of_terms
    last_term = terms[-1]

    res = F(number - last_term, terms[:-1]) + F(number, terms[:-1])
    return res


if __name__ == '__main__':
    NUMBER = 73
    TERMS = [1, 2, 3, 5, 10, 15, 20, 50]

    total_ways = number_to_limited_sum_of_terms(NUMBER, TERMS)

    print(total_ways)  # must be 4
