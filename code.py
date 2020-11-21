class GaussCode:
    def __init__(self, code, signing = None):
        self.code = code
        self.signing = signing
        self.nums = [1 if s == '+' else -1 for s in signing]
        self.signed = not not signing
