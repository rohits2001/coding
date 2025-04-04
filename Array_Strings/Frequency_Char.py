# 18. Find the frequency of characters
from collections import Counter
def char_frequency(s):
    return Counter(s)

a = "Hello World!"
result = char_frequency(a)
print(result)