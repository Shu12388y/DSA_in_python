def checkString(s1:str)->bool:
    return s1 == s1[::-1]




print(checkString("abc"))




# solution 2  


def checkStrings(s:str):
    low = 0
    high = len(s)-1
    while low < high:
        if s[low] != s[high]:
            print("no")
            break
        low += 1
        high -= 1
    else:
        print("yes")

checkStrings("aba")
