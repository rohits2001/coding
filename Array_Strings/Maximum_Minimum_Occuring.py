# 13. Determine whether one string is a rotation of another
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s1 in (s2 + s2)

a = "waterbottle"
result = is_rotation("erbottlewat", a)
print(result)