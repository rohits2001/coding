
# 3. Count the total number of vowels and consonants in a string
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = sum(1 for char in s if char in vowels)
    c_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return v_count, c_count

s = "Hello, World!"
print(count_vowels_consonants(s)) 