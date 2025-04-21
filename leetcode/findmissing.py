def findMissing(nums:list):
    sortedNums =  sorted(nums)
    for i in range(0,len(sortedNums)+1):
        if i not in sortedNums:
            return i

def findMissingNums(nums):
    n = len(nums)
    return n*(n+1)//2 - sum(nums)