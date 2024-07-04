def reverseString(s:str):
    word = s.split()
    res = word[::-1]
    s1 = " ".join(res)
    return s1

print(reverseString("abc"))

