# 5. Divide a string into 'N' equal parts
def divide_string(s, n):
    if len(s) % n != 0:
        return "Cannot divide equally"
    part_size = len(s) // n
    return [s[i:i + part_size] for i in range(0, len(s), part_size)]

a = ["a","b","c","d"]
result = divide_string(a, 2)
print(result)