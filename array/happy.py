# def checkChefHappy(s:str):
#     lst ='aeiou'
#     count = 0
#     for i in s:
#         for j in lst:
#             if i == j:
#                 count += 1
#         if count > 2:
#             return "Happy"
#     else:
#         return "Sad"


# print(checkChefHappy("aeiou")) 



# def checkHappy(s:str):
#     lts = {
#         'a':0,
#         'e':0,
#         'i':0,
#         'o':0,
#         'u':0
#     }
#     count = 0
#     for i in s:
#         if i in lts:
#             lts[i] += 1
#         else:
#             continue
#     for i in lts:
#         count += lts[i]
#         if(count > 2):
#             return "Happy"
#     else:
#         return "Sad"
    
# print(checkHappy("aeiou"))
# print(checkHappy("abxy"))
# print(checkHappy("aebcdefghij"))
# print(checkHappy("abcdeeafg"))


def checkContHappy(s:str):
    if len(s) < 5:
        return "Sad"
    vw = 'aeiou'
    count = 0
    for i in range(len(s)):
        for j in range(len(vw)):
            if s[i] ==  vw[j]:
                count += 1
                i += 1
        else:
            count = 0   
    if (count > 2):
        return "Happy"
    else:
        return "Sad"

print(checkContHappy("aeiou"))
print(checkContHappy("abxy"))
print(checkContHappy("aebcdefghij"))
print(checkContHappy("abcdeeafg"))