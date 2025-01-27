def twoSum(a:list,target:int)->int:
    lts = {}
    for i in range(len(a)):
        if a[i] not in lts:
            lts[a[i]] = i
    for i in lts:
        if target-i in lts:
            return [lts[i] ,lts[target-i]]
    return []


print(twoSum([2,7,11,15],9))