from collections import defaultdict

def twoSum(arr,target):
    hash  = dict()
    for i ,v in enumerate(arr):
        if(target-v in hash):
            return [hash[target-v],i]
        else:
            hash[v] = i
    return [-1,-1]



print(twoSum([2,7,11,15],18))