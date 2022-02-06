# FIXME use dynamic programming
def break_number_to_ordered_sum_of_terms(number: int, terms=None, memoize=None):
    """
        Assume number >= 0.
        Default terms from 1 to number - 1.
        Returns quantity of ordered sum of terms from "terms".
    """
    if number == 0:
        return 1
    if number < 0:
        return 0

    if terms is None:
        terms = [_ for _ in range(1, number)]

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

    N = 100
    quantity = break_number_to_ordered_sum_of_terms(N)
    print(quantity)
