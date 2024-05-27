def findX(nums:list)->int:
    for x in range(1,len(nums)+1):
        count = sum(1 for num in nums if num >= x)  
        if count == x:
            return x
    return -1    



print(findX([3,5]))


