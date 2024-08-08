# [1,1,2,3,4,5,3]  ==> (0,1),(3,6)


def goodPairs(l:list):
    result=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] == l[j]:
                result.append((i,j))
    return len(result)



print(goodPairs([1,1,1,1]))
