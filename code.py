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
        self.nums       = [1 if s == '+' else -1 for s in signing]
        self.signed     = not not signing
        self.indexes    = {}
        self.f          = 0
        self.orientable = True

        for i, l in enumerate(code):
            if l in self.indexes:
                self.indexes[l].append(i)
            else:
                self.indexes[l] = [i]

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
