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

        update_at_cursor(unique_terms, cursor, new_term)
        update_at_cursor(times_appear, cursor, current_sum // new_term)

        new_term = current_sum % new_term

        clean_to_cursor(unique_terms, cursor)
        clean_to_cursor(times_appear, cursor)

        # add last term which equals to new_term
        if new_term != 0:
            cursor += 1

            update_at_cursor(unique_terms, cursor, new_term)
            update_at_cursor(times_appear, cursor, 1)

        yield get_terms(unique_terms, times_appear)

def get_terms(unique_terms, times_appear):
    terms = []
    for i in range(len(times_appear)):
        times = times_appear[i]

        for j in range(times):
            terms.append(unique_terms[i])
    return terms

def update_at_cursor(members, cursor, to_add):
    if len(members) <= cursor:
        members.append(to_add)
    
    members[cursor] = to_add

def clean_to_cursor(to_clean, cursor):
    # to_clean = to_clean[:cursor + 1]

    len_to_erase = len(to_clean) - cursor - 1
    for i in range(len_to_erase):
        to_clean.pop()


if __name__ == '__main__':
    NUMBER = 7
    all_breakdowns = break_unorder_show(NUMBER)

    for breakdown in all_breakdowns:
        print(*breakdown)

    """
    7
    6 1
    5 2
    5 1 1
    4 3
    4 2 1
    4 1 1 1
    3 3 1
    3 2 2
    3 2 1 1
    3 1 1 1 1
    2 2 2 1
    2 2 1 1 1
    2 1 1 1 1 1
    1 1 1 1 1 1 1
    """
