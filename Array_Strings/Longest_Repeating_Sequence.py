# 7. Find the longest repeating sequence in a string
import re
def longest_repeating_sequence(s):
    for length in range(len(s) // 2, 0, -1):
        for i in range(len(s) - length):
            if s.count(s[i:i+length]) > 1:
                return s[i:i+length]
    return ""

a = "ababab"
result = longest_repeating_sequence(a)
print(result) 