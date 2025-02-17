def findDup(a:list):
    res = []
    if(len(a) == 1):
        return []
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                res.append(a[i])
    return [res]


print(findDup([1,2,3,4,4,1]))