from code import GaussCode

def succ(x):
    if isinstance(x, str):
        return chr(ord(x) + 1)

    return x + 1

def get_indexes(code, signing):
    n = len(code)

    indexes = {}

    for i in range(n):
        if code[i] in indexes:
            indexes[code[i]].append((signing[i], i))
        else:
            indexes[code[i]] = [(signing[i], i)]

    return indexes

def get_endings(code, signing, n):
    if len(code) == 2 * n:
        return [GaussCode(code, signing)]

    endings = []
    next_options = []

    # The old guys missing
    indexes = get_indexes(code, signing)
    one_rep = list(filter(lambda l: len(l) == 1, indexes.values()))

    op = lambda s: '-' if s == '+' else '+'
    next_options += [(code[e[0][1]], op(e[0][0])) for e in one_rep]

    # The next new guy
    if len(indexes) != n:
        new = succ(max(code))
        next_options += [(new, '+'), (new, '-')]

    for e in next_options:
        endings += get_endings(code + e[0], signing + e[1], n)

    return endings

def all_codes(n):
    return get_endings('a', '+', n)

codes = all_codes(2)

print(len(codes))

k = 0
s = set()

for c in codes:
    if c.euler == 2:
        print(c.code, c.signing)
        s.add(c.code)
        k += 1

print(k)
print(s)
