def findUnique(nums:list):
    res = 0 
    for i  in range(len(nums)):
        res  = res ^  nums[i]
    print(res)


findUnique([2,2,1])
findUnique([4,1,2,1,2])