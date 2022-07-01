"""
    S(n, k) = S(n - 1, k - 1) + k * S(n - 1, k), for 0 < k < n
    S(n, n) = 1, for n >= k
    S(n, 0) = 0, for n > 0
"""

def stirling_nums_second(n, k, /, *, memoize=None):
    if k > n:
        return -1

    if n < 0:
        return -2

    if n == k:
        return 1
    
    if k == 0:
        return 0

    return stirling_nums_second(n - 1, k - 1) + k * stirling_nums_second(n - 1, k)


if __name__ == '__main__':
    N = 4
    K = 2
    print(stirling_nums_second(N, K))  # should be 7
