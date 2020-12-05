from code import GaussCode

def succ(x):
    if isinstance(x, str):
        return chr(ord(x) + 1)

    return x + 1

def get_indexes(code):
    n = len(code)

    indexes = {}

    for i in range(n):
        if code[i] in indexes:
            indexes[code[i]].append(i)
        else:
            indexes[code[i]] = [i]

    return indexes

def get_endings(code, n):
    if len(code) == 2 * n:
        return [GaussCode(code)]

    endings = []
    next_options = []

    # The old guys missing
    indexes = get_indexes(code)
    one_rep = list(filter(lambda l: len(l) == 1, indexes.values()))
    next_options += [code[e[0]] for e in one_rep]

    # The next new guy
    if len(indexes) != n:
        next_options += [succ(max(code))]

    for e in next_options:
        endings += get_endings(code + e, n)

    return endings

def all_unsigned_codes(n):
    if n == 0:
        return [GaussCode('')]
    elif n == 1:
        return [GaussCode('aa')]

    return get_endings('ab', n)
