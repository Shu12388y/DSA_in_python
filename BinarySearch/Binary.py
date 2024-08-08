def Binary(l1:list,target:int):
    result = []
    for i in range(len(l1)):
        if l1[i]  == target:
            result.append(i)
    if len(result) == 0:
        return [-1,-1]
    else:
        return result


# Binary([1,2,3,4,9,8,8],8)        

print(Binary([1,2,4,3,8,8],8))      