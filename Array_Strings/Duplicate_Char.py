# 16. Find duplicate characters in a string
def duplicate_chars(s):
    return {char for char in s if s.count(char) > 1}

a = "Hello World!"
result = duplicate_chars(a)
print(result)