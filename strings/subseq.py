def substring(s1:str,s2:str)->bool:
    j = 0
    for i in range(len(s1)):
        if s1[i] == s2[j]:
            i += 1
            j += 1
            if j == len(s2):
                return True
        else:
            i += 1
    else:
        return False


print(substring("ABCDEF","AED"))

