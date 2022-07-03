def break_unorder_show(num):
    unique_terms = [num]
    times_appear = [1]

    yield get_terms(unique_terms, times_appear)

    cursor = 0
    while unique_terms[0] > 1:
        current_sum = 0

        # delete terms which equals to 1
        if unique_terms[cursor] == 1:
            current_sum += times_appear[cursor]
            cursor -= 1
        
        current_sum += unique_terms[cursor]
        times_appear[cursor] = times_appear[cursor] - 1

        new_term = unique_terms[cursor] - 1

        if times_appear[cursor] > 0:
            cursor += 1
        
        unique_terms[cursor] = new_term
        times_appear[cursor] = current_sum // new_term

        new_term = current_sum % new_term

        # add last term which equals to new_term
        if new_term != 0:
            cursor += 1

            if cursor >= len(unique_terms):
                unique_terms.append(new_term)
            if cursor >= len(times_appear):
                times_appear.append(1)

            unique_terms[cursor] = new_term
            times_appear[cursor] = 1

        yield get_terms(unique_terms, times_appear)

def get_terms(unique_terms, times_appear):
    terms = []
    for i in range(len(times_appear)):
        times = times_appear[i]

        for j in range(times):
            terms.append(unique_terms[i])
    
    return terms



if __name__ == '__main__':
    NUMBER = 7
    x = break_unorder_show(NUMBER)

    for i in x:
        print(i)
