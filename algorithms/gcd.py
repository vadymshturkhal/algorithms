def gcd(first: int, second: int):
    if second == 0:
        return first

    return gcd(second, first % second)


if __name__ == '__main__':
    a = 18
    b = 15
    print(gcd(a, b))
