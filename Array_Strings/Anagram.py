from collections import Counter
def are_anagrams(s1,s2):
    return Counter(s1) == Counter(s2)

a = "listen"
b = "silent"
print(are_anagrams(a,b)) 