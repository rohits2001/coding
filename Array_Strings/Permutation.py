# 8. Find all permutations of a string
from itertools import permutations
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

a = ["a","b"]
result = string_permutations(a)
print(result) 