# 23. Reverse string word by word
def reverse_words(s):
    return ' '.join(s.split()[::-1])

a = "This is a World!"
result = reverse_words(a)
print(result)