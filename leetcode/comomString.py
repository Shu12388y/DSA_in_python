# def commonString(words:list[str]) -> list[str]:
#     map = {}
#     aray=[]
#     for i in words:
#         for char in i:
#             if char in map:
#                 map[char] += 1
#             else:
#                 map[char] = 1
#     val = map.values()
#     for i in val:
#         if i%3 == 0:
#             aray.append(val.index(i))

#     return aray


# print(commonString(["bella","label","roller"]))




def string(s):
    word = set(s[0])
    return word

print(string(["bella","label","roller"]))    


def commonChars(self, words: List[str]) -> List[str]:
    if len(words) < 2:
        return words
    res = []
    word1 = set(words[0])
    for char in word1:
        frequency = min([word.count(char) for word in words])
        res += [char] * frequency
    return res 