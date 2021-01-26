from string import abc
from copy   import deepcopy
from code   import GaussCode

class PartialCode:
    def __init__(self, code):
        self.code = code
        self.indexes = {}

        for i, l in enumerate(code):
            self.register(l, i)

    def __iter__(self):
        return iter((self.code, self.indexes))

    def register(self, letter, index):
        if letter in self.indexes:
            self.indexes[letter].append(index)
        else:
            self.indexes[letter] = [index]

    def add(self, letter):
        self.register(letter, len(self.code))
        self.code += [letter]

    def __repr__(self):
        if len(self.code) // 2 > len(abc):
            return str(self.code)

        return ''.join([abc[k] for k in self.code])

def get_candidates(partial, v):
    code, inds  = partial
    n           = len(code)

    def f(pair):
        ind, letter = pair

        parity_cond = ind % 2 != n % 2
        one_rep     = len(inds[letter]) == 1
        non_bigon   = True

        if len(inds[code[-1]]) == 2:
            ind = inds[code[-1]][0]

            if letter == code[(ind + 1) % n]:
                non_bigon = False

            if letter == code[(ind - 1) % n]:
                non_bigon = False

        return parity_cond and one_rep and non_bigon

    next        = max(partial.code) + 1 if len(partial.code) else 0
    candidates  = list(filter(f, enumerate(partial.code[:-1])))
    candidates  = [c[1] for c in candidates]

    if next < v:
        candidates.append(next)

    if n == 2 * v - 1:
        candidates

    return candidates

def get_endings(partial, v):
    if len(partial.code) == 2 * v:
        return [partial]

    endings = []
    candidates = get_candidates(partial, v)

    for c in candidates:
        new_partial = deepcopy(partial)
        new_partial.add(c)
        endings += get_endings(new_partial, v)

    return endings

def all(v):
    partials = get_endings(PartialCode([]), v)

    for p in partials:
        gauss_code = GaussCode(p.code)

        if gauss_code.euler() == 2:
            print(gauss_code.code)

all(10)

'''

[0, 1, 2, 3, 4, 0, 5, 6, 3, 7, 1, 5, 8, 4, 7, 2, 6, 8]
[0, 1, 2, 3, 4, 0, 5, 6, 3, 7, 1, 8, 6, 4, 7, 2, 8, 5]
[0, 1, 2, 3, 4, 5, 1, 6, 3, 7, 5, 0, 8, 4, 7, 2, 6, 8]
[0, 1, 2, 3, 4, 5, 1, 6, 3, 7, 5, 8, 6, 2, 7, 4, 8, 0]
[0, 1, 2, 3, 4, 5, 1, 6, 7, 4, 8, 2, 6, 0, 5, 8, 3, 7]
[0, 1, 2, 3, 4, 5, 6, 2, 7, 0, 5, 8, 3, 7, 1, 6, 8, 4]
[0, 1, 2, 3, 4, 5, 6, 2, 7, 4, 8, 6, 1, 7, 3, 8, 5, 0]

[0, 1, 2, 3, 4, 0, 5, 6, 7, 2, 8, 4, 6, 9, 1, 8, 3, 7, 9, 5]
[0, 1, 2, 3, 4, 5, 1, 6, 3, 7, 5, 8, 9, 0, 8, 4, 7, 2, 6, 9]
[0, 1, 2, 3, 4, 5, 1, 6, 7, 4, 8, 2, 6, 0, 9, 7, 3, 8, 5, 9]
[0, 1, 2, 3, 4, 5, 1, 6, 7, 4, 8, 2, 6, 9, 5, 8, 3, 7, 9, 0]
[0, 1, 2, 3, 4, 5, 1, 6, 7, 4, 8, 2, 9, 7, 5, 8, 3, 9, 6, 0]
[0, 1, 2, 3, 4, 5, 6, 0, 5, 7, 3, 8, 1, 9, 7, 4, 8, 2, 9, 6]
[0, 1, 2, 3, 4, 5, 6, 0, 7, 2, 8, 4, 9, 6, 1, 7, 3, 8, 5, 9]
[0, 1, 2, 3, 4, 5, 6, 0, 7, 4, 8, 2, 9, 7, 5, 8, 3, 9, 1, 6]
[0, 1, 2, 3, 4, 5, 6, 2, 7, 0, 8, 4, 9, 6, 1, 7, 3, 9, 5, 8]
[0, 1, 2, 3, 4, 5, 6, 2, 7, 4, 8, 6, 1, 9, 5, 8, 3, 7, 9, 0]
[0, 1, 2, 3, 4, 5, 6, 2, 7, 4, 8, 6, 9, 0, 5, 8, 3, 7, 1, 9]
[0, 1, 2, 3, 4, 5, 6, 2, 7, 8, 5, 9, 3, 7, 1, 6, 9, 4, 8, 0]

The algorithm is bugged, it doesn't work on the border case.

'''
