# [1,2,4]
# [4,3,2]  -->  [1,3]

def findSet(a:list,b:list):
    res = []
    for i in a:
        if i in b:
            pass
        else:
            res.append(i)
    for i in b:
        if i in a:
            pass 
        elif i in res:
            pass
        else:
            res.append(i)
    return res


def findSets(a:list, b:list):
    seta = set(a)
    setb =  set(b)
    return seta  ^ setb



findSet([1,2,4],[4,3,2,5])    

print(findSets([1,2,4],[4,3,2,5]))    
