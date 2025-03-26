def triple(nums):
    # sorted it
    soretedNums = sorted(nums)
    # create set as duplicate element is there
    tupleSet = set(soretedNums)
    if(len(tupleSet) > 2):
        return len(tupleSet)
    else:
        return 0


print(triple([4,4,2,4,3]))
print(triple([1,1,1,1,1]))