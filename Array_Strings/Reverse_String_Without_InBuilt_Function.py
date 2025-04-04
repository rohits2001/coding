# 24. Reverse string without using the reverse() function
def manual_reverse(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

a = "This is a World!"
result = manual_reverse(a)
print(result)