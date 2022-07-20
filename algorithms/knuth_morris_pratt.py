def knuth_morris_pratt(string, pattern):
    dfa = create_dfa_from_pattern(pattern)

    for char in string:
        pass

def create_dfa_from_pattern(pattern):
    pass


if __name__ == '__main__':
    string = 'ababac'
    knuth_morris_pratt(string, 'baba')
