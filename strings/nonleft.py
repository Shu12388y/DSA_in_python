def nonLeft(s1:str):
    for i in range(len(s1)):
        flag = False
        for j in range(i+1,len(s1)):
            if s1[i] == s1[j]:
                flag = True
                break
        if flag == False:
            return i 
    return -1
   



print(nonLeft("acba"))


# solution  2 T.C. O(n)  S.C. O(256)
def hashedFirst(s1:str):
    count = [0]*256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
    for i in range(len(s1)):
        if count[ord(s1[i])] == 1:
            return i 
    else:
        return -1



print(hashedFirst("acba"))





# solution 3  


def hashedFast(s1:str):

