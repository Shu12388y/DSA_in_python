# worst solution   10^3

def reverseString(s1:str,s2:str)->bool:
    str1 = [i for i in s1]
    str2 = [i for i in s2]
    for _ in range(len(str1)):
        temp = ''
        count = 0
        for j in range(len(str1)):
            numRotate = 0
            if str1[j] == str2[j]:
                count += 1
            if count == len(str1):
                return True
        else:
            temp = str1[0]
            str1.remove(str1[0])
            str1.append(temp)
            numRotate = numRotate + 1
            print(str1)
            print(str2)
            print(numRotate)
            
    else:
        return False

print(reverseString("abcd","cdab"))





# best solution

# time complexity is O(n)
# space complexity is O(1)

def findRotation(s1:str,s2:str)->bool:
    if len(s1) != len(s2):
        return False
    else:
        temp = ''
        temp = s1+s1
        return temp.find(s2)  != -1
