from collections    import deque
from collections    import namedtuple
from code           import GaussCode

Dart = namedtuple('Dart', 'index dir')

def euler(signed_code):
    code    = signed_code.code
    signing = signed_code.nums
    n       = len(code)
    darts   = {}
    indexes = {}

    for i, l in enumerate(code):
        if l in indexes:
            indexes[l].append(i)
        else:
            indexes[l] = [i]

    def succ(dart):
        index, dir  = dart
        k           = (index + dir) % n
        sign        = signing[k]
        pair        = indexes[code[k]]
        other       = list(filter(lambda i: i != k, pair))[0]

        return Dart((other + sign * dir) % n, (-1) * sign * dir)

    def flip(dart):
        index, dir = dart

        return Dart((index + dir) % len(code), (-1) * dir)

    f = 0

    crypt = lambda dart: str(dart.dir * (dart.index + 1))

    for i in range(n):
        for d in [-1, 1]:
            dart = Dart(i, d)

            if not crypt(dart) in darts:
                while not crypt(dart) in darts:
                    darts[crypt(dart)] = f
                    dart = flip(succ(dart))

                if dart.index != i or dart.dir != d:
                    return 'non-planar'

                f += 1

    faces = len(set(darts.values()))

    return faces - int(n / 2)

print('abcabc', '\n-+-+-+')
print(euler(GaussCode('abcabc', '-+-+-+')))
