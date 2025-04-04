# 11. Replace spaces in a string with a specific character
def replace_spaces(s, char):
    return s.replace(" ", char)

a = "Hello World!"
result = replace_spaces(a, "%20")
print(result) 