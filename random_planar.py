from code import GaussCode

import numpy as np

def random_planar_signed(v):
    euler = 0
    while euler != 2:
        n = np.random.randint(1, v)

        pos = [(i, '+') for i in range(n)]
        neg = [(i, '-') for i in range(n)]

        code = np.array(pos + neg)
        np.random.shuffle(code)
        gauss_code = GaussCode(list(code.T[0]), list(code.T[1]))
        euler = gauss_code.euler

    return gauss_code

print(random_planar_signed(20))

'''
has_empty_loops = False

for k in range(n):
    diff = gauss_code.indexes[k][1] - gauss_code.indexes[k][0]

    if abs(diff) == 1:
        has_empty_loops = True

inds = gauss_code.indexes
has_empty_loops_or_bigons = False

for k in range(n):
    neighbors = set()

    neighbors.add(gauss_code.code[(inds[str(k)][0] + 1) % (2 * n)])
    neighbors.add(gauss_code.code[(inds[str(k)][0] - 1) % (2 * n)])
    neighbors.add(gauss_code.code[(inds[str(k)][1] + 1) % (2 * n)])
    neighbors.add(gauss_code.code[(inds[str(k)][1] - 1) % (2 * n)])

    print(gauss_code)
    print(k)
    print(neighbors)
    exit()

    if len(neighbors) != 4:
        has_empty_loops_or_bigons = True

iters += 1
'''
