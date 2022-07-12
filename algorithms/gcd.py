def gcd(first: int, second: int):
    if first < 0 or second < 0:
        return
    
    if type(first) != int or type(second) != int:
        return

    if second == 0:
        return first

    return gcd(second, first % second)


if __name__ == '__main__':
    print(gcd(119, 544))
    print(gcd(-119, 544))
    print(gcd(119.111, 544))
