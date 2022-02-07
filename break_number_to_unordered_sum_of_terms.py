def break_number_to_unordered_sum_of_pairs(number: int):
    """
        Assume number >= 0.
        Default terms from 1 to number.
        Returns quantity of unordered sum of terms from "terms".
        Theorem:
            F(n: [n1, n2,...,nk]) = F(n - n1: [n1, n2,...,nk]) + F(n: [n2,...,nk])
    """
    return 0


if __name__ == '__main__':
    N = 3
    quantity = break_number_to_unordered_sum_of_pairs(N)
    print(quantity)
