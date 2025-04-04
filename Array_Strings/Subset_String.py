from itertools import combinations
def string_subsets(s):
    subsets = []
    for i in range(1, len(s) + 1):
        subsets.extend([''.join(c) for c in combinations(s, i)])
    return subsets

a = "abc"
result = string_subsets(a)
print(result)