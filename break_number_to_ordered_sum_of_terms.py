# FIXME use dynamic programming
def break_number_to_ordered_sum_of_terms(number: int, terms=None):
    """
        Assume number >= 0.
        Default terms from 1 to number - 1.
    """
    if number == 0:
        return 1
    if number < 0:
        return 0

    if terms is None:
        terms = [_ for _ in range(1, number)]
        memoize = {}

    current_sum = 0
    for term in terms:
        current_term = number - term
        current_sum += break_number_to_ordered_sum_of_terms(current_term, terms)

    return current_sum


if __name__ == '__main__':
    N = 3
    quantity = break_number_to_ordered_sum_of_terms(N)
    print(quantity)

    a = {}
