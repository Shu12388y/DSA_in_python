def findDup(a:list):
    nums = set(a)
    print(nums)
    if len(nums) != len(a):
        return False
    return True


print(findDup([1,2,3,1]))