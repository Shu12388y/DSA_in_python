# solution 1   O(n^2)

def checkAnagram(s1:str,s2:str)->bool:
    count = 0
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                count += 1
        if count == len(s2):
            return True
    else:
        return False


print(checkAnagram("aab","abb"))


# solution 2   O(nlogn)

def checkAnagram2(s1:str,s2:str)->bool:
    if len(s1)  != len(s2):
        return False
    else:
        str1 = sorted(s1)
        str2 =  sorted(s2)
        return str1 == str2


print(checkAnagram2("aab","bba"))



# solution 3 using a hashed array
# time complexity O(n)


def hashedString(s1:str,s2:str)->bool:
    if len(s1) != len(s2):
        return False
    count  = [0]*256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])]  -= 1
    for x in count:
        if x != 0:
            return False 
    return True
