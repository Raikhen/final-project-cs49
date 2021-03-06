from code           import GaussCode
from all            import all_codes
from unsigned_all   import all_unsigned_codes

'''
Proper toroidal:
    abcabdecde

Proper 2-toroidal:
    abcdaefbefdgcg
    abcdafdegfbhgceh
    ajkchijbgpiafophenogdmnfclmebkld (satisfies parity condition)

Proper 3-toroidal:
    abacdedbfcfe
'''

codes = all_unsigned_codes(4)
print(len(codes))

best_code = ''
best_euler = 4

for c in codes:
    euler = c.euler()

    if euler < best_euler:
        best_code = c
        best_euler = euler
        print(best_code, best_euler)

print('Done.\n')

'''
Sequence A

Smallest number of vertices required to be minimally embeddable on genus g:
0) 0, with ''.
1) 2, with 'abab'.
2) 5, with 'ababcdcede'.
3) 6, with 'abacdedbfcfe'.
4) >7.
'''

codes = all_codes(4)
print(len(codes))

best_code = ''
best_euler = 4

for c in codes:
    if c.euler < best_euler:
        best_code = c
        best_euler = c.euler
        print(best_code)

'''
Sequence B

Smallest number of vertices with signing required to be min. emb. on genus g:
0) 0, with ('', '').
1) 2, with ('abab', '++--')
2) 3, with ('abacbc', '++---+')
3) 5, with ('ababcdeced', '++--+++---')
4) 7, with ('ababcdcdefegfg', '++--++--++---+').
'''

# Clearly, we have that sequence A is stricly greater than sequence B.
