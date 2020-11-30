from code import GaussCode

code = GaussCode('abcabc')
code.compute_all_signings()
print(code.euler())
