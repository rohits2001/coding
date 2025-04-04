# 19. Find the largest and smallest word in a string
def largest_smallest_word(s):
    words = s.split()
    return max(words, key=len), min(words, key=len)

a = "This is a World!"
result = largest_smallest_word(a)
print(result)