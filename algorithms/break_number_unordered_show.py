def break_unorder_show(num):
    unique_terms = [num]
    times_appear = [1]

    yield get_terms(unique_terms, times_appear)


def get_terms(unique_terms, times_appear):
    terms = []
    for i in range(len(times_appear)):
        times = times_appear[i]

        for i in range(times):
            terms.append(unique_terms[i])
    
    return terms



if __name__ == '__main__':
    NUMBER = 7
    x = break_unorder_show(NUMBER)

    for i in x:
        print(i)
