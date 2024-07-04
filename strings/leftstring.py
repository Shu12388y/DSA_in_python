# using two for loop T.C. O(n^2)

def findfirst(s1:str)->int:
    for i in range(len(s1)):
        first = s1[i]
        for j in range(i+1,len(s1)):
            if first == s1[j]:
                return s1.index(first)
    else:
        return -1

print(findfirst("abcd"))





# solution 2 using hashed array  T.C. O(n)


def findfirstHash(s1:str)->int:
    count = [0]*256
    for i in range(len(s1)):
        count[ord(s1[i])]  += 1
    for i in range(len(s1)):
        if count[ord(s1[i])] > 1:
            return i
    else:
        return -1



# solution 3 using hashed boolean array
#

def booleanHash(s1:str):
    count = [False]*256
    res = -1
    for i in range(len(s1),-1,-1):
        if count[ord(s1[i])] == True:
            res = i
        else:
            count[ord(s1[i])] = True 
    return res        
