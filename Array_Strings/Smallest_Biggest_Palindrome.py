# 22. Find the smallest and biggest palindrome word in a string
def smallest_biggest_palindrome(s):
    words = s.split()
    palindromes = [word for word in words if word == word[::-1]]
    return min(palindromes, key=len, default=""), max(palindromes, key=len, default="")

a = "This is a World! madam radar"
result = smallest_biggest_palindrome(a)
print(result)