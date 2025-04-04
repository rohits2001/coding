# 17. Find duplicate words in a string
def duplicate_words(s):
    words = s.split()
    return {word for word in words if words.count(word) > 1}

a = "Hello World! Hello World!"
result = duplicate_words(a)
print(result)