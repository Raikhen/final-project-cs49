from code import GaussCode

code = GaussCode('8156237845126734')
code.compute_all_signings()
print(code.euler())

# aijafnebjkbgopihemnofcklchpgdlmd
# acedbabcde

'''
Proper toroidal:
    abcabdecde

Proper 2-toroidal:
    abcdaefbefdgcg
    abcdafdegfbhgceh
    ajkchijbgpiafophenogdmnfclmebkld (satisfies parity condition)
'''
