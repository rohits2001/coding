# 21. Swap two string variables without using a third variable
def swap_strings(a, b):
    a, b = b, a
    return a, b

a = "Hello"
b = "World"
result = swap_strings(a, b)
print(result)