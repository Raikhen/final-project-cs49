from copy           import deepcopy
from collections    import namedtuple

Dart = namedtuple('Dart', 'index dir')

class GaussCode:
    def succ(self, dart):
        index, dir  = dart
        k           = (index + dir) % self.e
        sign        = self.nums[k]
        pair        = self.indexes[self.code[k]]
        other       = list(filter(lambda i: i != k, pair))[0]

        return Dart((other + sign * dir) % self.e, (-1) * sign * dir)

    def flip(self, dart):
        index, dir = dart

        return Dart((index + dir) % self.e, (-1) * dir)

    def __init__(self, code, signing = None):
        self.code       = code
        self.signing    = signing
        self.e          = len(code)
        self.v          = len(code) // 2
        self.signed     = not not signing
        self.indexes    = {}

        for i, l in enumerate(code):
            if l in self.indexes:
                self.indexes[l].append(i)
            else:
                self.indexes[l] = [i]

        if self.signed:
            self.nums       = [1 if s == '+' else -1 for s in signing]
            self.f          = 0
            self.orientable = True

            darts = {}
            crypt = lambda dart: str(dart.dir * (dart.index + 1))

            for i in range(self.e):
                for d in [-1, 1]:
                    dart = Dart(i, d)

                    if not crypt(dart) in darts:
                        while not crypt(dart) in darts:
                            darts[crypt(dart)] = self.f
                            dart = self.flip(self.succ(dart))

                        if dart.index != i or dart.dir != d:
                            self.orientable = False

                        self.f += 1

            self.euler = self.v - self.e + self.f

    def uncrossed(self):
        s = deepcopy(self.code)

        intersections = list(self.indexes.keys())

        for i in intersections:
            i_1 = s.index(i) + 1
            i_2 = s[i_1:].index(i) + i_1
            s   = s[:i_1] + s[i_1:i_2][::-1] + s[i_2:]

        return s

    def compute_all_signings(self):
        def chain(n):
            if n == 0:
                return ['']

            cs = chain(n - 1)
            return [f'+{c}' for c in cs] + [f'-{c}' for c in cs]

        signings = []

        for c in chain(self.v):
            s = ['-'] * self.e

            for i, l in enumerate(self.indexes.keys()):
                i_1 = self.indexes[l][0]
                i_2 = self.indexes[l][1]

                if c[i] == '+':
                    s[i_1] = '+'
                else:
                    s[i_2] = '+'

            signings.append(''.join(s))

        self.all = signings

    def euler(self):
        if self.signed:
            return self.euler

        self.compute_all_signings()

        return max([GaussCode(self.code, s).euler for s in self.all])

    def __repr__(self):
        s = self.code

        if self.signed:
            s += f'\n{self.signing}\neuler = {self.euler}\n'

        return s
