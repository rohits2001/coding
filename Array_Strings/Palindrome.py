# 12. Determine whether a given string is palindrome
def is_palindrome(s):
    return s == s[::-1]

a = "racecar"
result = is_palindrome(a)
print(result)