def break_number_to_ordered_sum_of_terms(number: int, terms=None, memoize=None):
    """
        Assume number >= 0.
        Default terms from 1 to number.
        Returns quantity of ordered sum of terms from "terms".
        Theorem:
            F(n: [n1, n2,...,nk]) = F(n - n1: [n1, n2,...,nk])
            + F(n - n2: [n1, n2,...,nk])
            + ...
            + F(n - nk: [n1, n2,...,nk]).
            F(0: [n1, n2,...,nk]) = 1.
            F(-n: [n1, n2,...,nk]) = 0
        Theorem:
            F(n: [n1, n2,...,nk]) = 2**(n - 1)
    """
    if number == 0:
        return 1
    if number < 0:
        return 0

    if terms is None:
        terms = [_ for _ in range(1, number + 1)]

    if memoize is None:
        memoize = {}

    current_sum = 0
    for term in terms:
        current_term = number - term
        if memoize.get(current_term) is None:
            current_sums_quantity = break_number_to_ordered_sum_of_terms(current_term, terms, memoize)
            memoize[current_term] = current_sums_quantity
        else:
            current_sums_quantity = memoize[current_term]

        current_sum += current_sums_quantity

    return current_sum


if __name__ == '__main__':
    N = 3
    quantity = break_number_to_ordered_sum_of_terms(N)
    print(quantity)

    N = 5
    quantity = break_number_to_ordered_sum_of_terms(N)
    print(quantity)
