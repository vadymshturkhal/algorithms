def break_unorder_show(num):
    unique_terms = [_ for _ in range(num, 0, -1)]
    how_many_times_appear = [0 for _ in range(1, num + 1)]
    print(unique_terms)
    print(how_many_times_appear)


if __name__ == '__main__':
    NUMBER = 7
    break_unorder_show(NUMBER)
