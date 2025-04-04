#2. Count the total number of punctuation characters in a string
import string
def count_punctuation(s):
    return sum(1 for char in s if char in string.punctuation)

a = "Hello World! How are you?"
result = count_punctuation(a)
print(result)