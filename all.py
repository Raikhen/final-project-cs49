import string
from itertools  import permutations
from code       import GaussCode

ABC = string.ascii_lowercase
v = 3

l = [ABC[i] + '+' for i in range(v)] + [ABC[i] + '-' for i in range(v)]
print(l)

raw = list(permutations(l))

print(len(raw))

surfaces = {'0': 0, '2': 0, '-2': 0, '-4': 0}

for tup in raw:
    letters = ''.join([s[0] for s in tup])
    signing = ''.join([s[1] for s in tup])
    code    = GaussCode(letters, signing)

    surfaces[str(code.euler)] += 1

print(surfaces)

'''
Without correcting for overcounting:

0) {'0': 0, '2': 1, '-2': 0, '-4': 0}
1) {'0': 0, '2': 2, '-2': 0, '-4': 0}
2) {'0': 8, '2': 16, '-2': 0, '-4': 0}
3) {'0': 396, '2': 252, '-2': 72, '-4': 0}
4) {'0': 21216, '2': 6240, '-2': 12864, '-4': 0}
5) {'0': 1322400, '2': 215520, '-2': 1831680, '-4': 259200}
'''
